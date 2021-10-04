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
        new_news = news_service.getNaverSearchNews('셀트리온', page_count, 30)
        df = news_service.DFconcat(df, new_news)

    days_2ago = (dt.datetime.today() - dt.timedelta(days=2)).strftime('%Y-%m-%d')
    df = df[df['pubDate'] >= days_2ago].reset_index(drop=True)
    print("df 길이는 ---------> ", len(df))

    # 형태소 분석
    df = news_service.morphs_nlp(df)

    # 평균점수
    score_mean = news_service.predict_score(df)
    # 긍부정 비율
    positive_ratio = news_service.ratio['positive_ratio']
    negaitive_ratio = news_service.ratio['negaitive_ratio']
    # 워드클라우드용 긍부정 데이터 수
    pos_word30 = news_service.pos_neg[0]
    neg_word30 = news_service.pos_neg[1]

    print(positive_ratio, " / ", negaitive_ratio)

    return {'score_mean': score_mean, 'positive_ratio': positive_ratio, 'negaitive_ratio': negaitive_ratio, 'pos_word30': pos_word30, 'neg_word30': neg_word30}
