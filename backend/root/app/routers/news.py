import pandas as pd
from fastapi import APIRouter
from ..exception.handler import handler
import datetime as dt
from ..service.news_service import news_service

router = APIRouter()


@router.get("/{search_word}")
async def news_predict(search_word: str):
    print("search_word : ", search_word)
    if search_word is None:
        handler.code(404)
    df = pd.DataFrame(columns=['title', 'description', 'originallink', 'link', 'pubDate'])
    print("df : ", df)

    page_count = 1
    new_news = news_service.getNaverSearchNews(search_word, page_count, 30)
    df = news_service.DFconcat(df, new_news)

    while news_service.checkDate(df):
        page_count += 1
        new_news = news_service.getNaverSearchNews(search_word, page_count, 30)
        df = news_service.DFconcat(df, new_news)

    days_2ago = (dt.datetime.today() - dt.timedelta(days=2)).strftime('%Y-%m-%d')
    # 분석기사 수 200개 제한
    df = df[df['pubDate'] >= days_2ago].reset_index(drop=True)[:200]
    print("df 길이는 200! ---------> ", len(df))

    # 형태소 분석
    df = news_service.morphs_nlp(df)
    print('### df[0]: ', df.iloc[0])
    # 평균점수
    score_mean = news_service.predict_score(df)
    print('### score_mean: ', score_mean)

    # 긍부정 비율
    ratio = news_service.ratio(df)
    positive_ratio = ratio['positive_ratio']
    negaitive_ratio = ratio['negaitive_ratio']

    # 워드클라우드용 긍부정 기사수
    pos_neg = news_service.pos_neg(df)
    pos_count= pos_neg['pos_count']
    neg_count = pos_neg['neg_count']
    word_cloud30 = pos_neg['word_cloud30']
    pos_link = pos_neg['pos_link']
    neg_link = pos_neg['neg_link']

    return {'total_count': len(df), 'score_mean': score_mean,
            'positive_ratio': positive_ratio, 'negaitive_ratio': negaitive_ratio,
            'pos_count': pos_count, 'neg_count': neg_count, 'word_cloud30': word_cloud30,
            'pos_link': pos_link, 'neg_link': neg_link }
