from urllib import request, parse

class Naver:

    news_url = 'https://openapi.naver.com/v1/search/news.json'
    client_id = 'XtnzmNJ9jTScRPlMth2a'
    client_secret = 'nYviyHz2K8'

    def get_news(self, query, start=1):

        query_param = {}
        query_param['display'] = 100
        query_param['start'] = start
        query_param['query'] = query
        query_param['sort']='sim'
        
        url_query = self.news_url + '?' + parse.urlencode(query_param)
        print(url_query)

        self.send(url_query)
        
    
    def send(self, url_query):
        req = request.Request(url_query)
        req.add_header("X-Naver-Client-Id", self.client_id)
        req.add_header("X-Naver-Client-Secret", self.client_secret)

        res = request.urlopen(req)

        res_code = res.getcode()


        if res_code == 200:
            print(res.read().decode('utf-8'))
            return res.read()
        else:
            print("Naver Search Error!!! code=", res_code)
            print(res.read().decode('utf-8'))
            

            
naver_search = Naver()