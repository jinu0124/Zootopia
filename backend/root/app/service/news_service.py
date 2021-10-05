import os
import numpy as np
from collections import Counter
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
import re
from tensorflow.keras.models import load_model
from konlpy.tag import Okt
import datetime as dt
import requests
import pandas as pd

class News:

    global client_id
    global client_secret
    client_id = "vKllKxKbERYB7fpkEQO4"
    client_secret = "K4jATtYNtv"
    global days_2ago
    days_2ago = (dt.datetime.today() - dt.timedelta(days=2)).strftime('%Y-%m-%d')

    # def __init__(self):
    #     filename = os.getcwd() + "app/service/news_model.h5"
    #     score_model = load_model(filename)

    def getNaverSearchNews(self, search_word, page_start, display):
        headers = {'X-Naver-Client-Id' : client_id,
                   'X-Naver-Client-Secret':client_secret
                   }
        search_word = search_word
        encode_type = 'json'
        max_display = display
        sort = 'date' #결과값의 정렬기준 시간순 date, 관련도 순 sim
        start = page_start
        url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"

        #HTTP요청 보내기
        r = requests.get(url, headers=headers)
        #요청 결과 보기 200 이면 정상적으로 요청 완료

        new_df = pd.DataFrame(r.json()['items'])
        new_df= new_df[new_df['title'].str.contains(search_word)]
        new_df['pubDate'] = [ dt.datetime.strptime(x[5:16], "%d %b %Y").strftime('%Y-%m-%d') for x in new_df['pubDate'] ]
        if (r == None):
            return None
        else:
            return new_df

    def DFconcat(self, df, df_add):
        df = pd.concat([df, df_add])
        return df

    def checkDate(self, df):
        if (df.iloc[-1, -1] < days_2ago) or (len(df) > 200):
            return False
        else: return True

    def morphs_nlp(self, df):
        # 불용어
        stopwords = ['오늘','어떻다','년도','만에','오전', '오후','까지', '이후', '분기', '오다', '가다', '기업','지수','대한','최근','대비','지난','연구원','지난','투자','통해','주가','만원','거래','거래','따르다','조억원','억원','되다','다소','약간','하고','했고','매우','많이','가장','돼다','이고','였다','였고','이다','이라고','이라는','있다','있었다','의','가','이','은','을','들','는','좀','잘','걍','과','도','를','으로','자','에','에서','와','한','하다',
                    '주식','가격','시장','증권','한국','미국','중국','금융','코스피','코스닥','애플','부터','br', '/><', '/>', '.<', '<b>', '</b>']
        morphs = []
        okt = Okt()
        data = df['description']
        data = [re.sub('[^A-Za-z가-힣 ]', '', sentence) for sentence in data] #한글 영어만

        for row in data:
            morphs_x = okt.morphs(row, stem=True) # 형태소 단위 토큰화
            morphs_x = [word for word in morphs_x if not word in stopwords] # 불용어 제거
            morphs_x = [word for word in morphs_x if not len(word)< 2 ] # 한글자는 필요없을거같아서 삭제
            morphs.append(morphs_x)

        # 원래 df에 컬럼 추가
        df['tokenized'] = morphs
        return df

    def pos_neg(self, df):
        pos = len(df[df.score > 0.5])
        neg = len(df[df.score < 0.5])
        total_words = np.hstack(df['tokenized'].values)

        pos_link = df[df.score > 0.6]['link'][:10]
        neg_link = df[df.score > 0.6]['link'][:10]

        word_count = Counter(total_words)
        word_cloud30 = word_count.most_common(30)
        return {'pos_count': pos, 'neg_count': neg, 'word_cloud30': word_cloud30, 'pos_link': pos_link, 'neg_link': neg_link }

    def predict_score(self, df):
        test_x = df['tokenized'].values
        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(test_x)
        threshold = 2

        total_cnt = len(tokenizer.word_index)
        vocab_size = total_cnt

        # 단어 집합 수 맞추기
        while vocab_size > 2600:
            rare_cnt = 0 # 빈도수가 threshold보다 작은 단어의 개수를 카운트
            total_freq = 0 # 총 단어 빈도수 총 합
            rare_freq = 0 # 등장 빈도수가 threshold보다 작은 단어의 등장 빈도수의 총 합

            for key, value in tokenizer.word_counts.items():
                total_freq = total_freq + value

                # 단어의 등장 빈도수가 threshold보다 작으면
                if value < threshold:
                    rare_cnt += 1
                    rare_freq = rare_freq + value
            threshold += 1

            vocab_size = total_cnt - rare_cnt + 2
            print('단어 집합의 크기 :', vocab_size)

        tokenizer = Tokenizer(vocab_size, oov_token = 'OOV')
        tokenizer.fit_on_texts(test_x)
        test_x = tokenizer.texts_to_sequences(test_x)

        # 크롤링 페이지의 기사 길이 확인하고 수정하기!!!!!!!!!!!!!!!!!!!!!!!111
        max_len = max(len(l) for l in test_x)
        test_x = pad_sequences(test_x, maxlen = max_len)
        ## ---

        filename = "C:/Users/multicampus/Documents/S05P21A602/backend/root/app/service/news_model.h5"
        score_model = load_model(filename)

        score = score_model.predict(test_x)
        score = score.tolist()
        score = sum(score, [])

        df['score'] = score

        return df

    def today_score(self, df):
        score_mean = np.mean(df['score'])
        return score_mean

    def date_score(self, df):
        date_mean = df[['pubDate','score']].groupby('pubDate').mean().reset_index(drop=False)
        return date_mean

    def ratio(self, df):
        positive_ratio = len(df[df['score'] >= 0.51])/len(df)*100
        negaitive_ratio = len(df[df['score'] < 0.51])/len(df)*100

        print('긍정 기사 비율 : ', positive_ratio, "% ")
        print('부정 기사 비율 : ', negaitive_ratio, "% ")
        return {'positive_ratio': positive_ratio, 'negaitive_ratio': negaitive_ratio}


news_service = News()