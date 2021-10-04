from bs4 import BeautifulSoup
import requests
from urllib.parse import urlencode, urlparse, urljoin

from datetime import datetime, timedelta


class Finance_news:

    url = 'https://finance.naver.com/item/news_news.nhn' 

    def crawler(self, company_code, max_page, custom_timedelta = timedelta(days=1)):

        query_param = {}
        query_param['code'] = company_code

        url_info = urlparse(self.url)

        for page in range(1, max_page+1):
            query_param['page'] = page
            query = urlencode(query_param)

            res = requests.get(self.url + '?' + query).text
            html = BeautifulSoup(res, "lxml")

            # print(html)

            title_tag = html.select('.title')

            titles = []
            links = []
            publishers = [ pub.get_text().strip() for pub in html.select('.info')]
            dates   = [date.get_text().strip() for date in html.select('.date')]
            contents = []

            # 제목과 링크
            for tag in title_tag:
                titles.append(tag.a.get_text().strip())
                links.append(urljoin(self.url,tag.a.get('href')))
            
            today = datetime.today()

            for i in range(0, len(dates)):
                newsdate = datetime.strptime(dates[i], "%Y.%m.%d %H:%M")

                # 제한날짜 이내에 뉴스기사들만 넣기
                if (today - newsdate) >= custom_timedelta:
                    break
                
                # 콘텐트
                # content_res = requests.get(links[i]).text
                # content_html = BeautifulSoup(content_res, "lxml")
                # contents.append(content_html.select_one('#news_read').get_text())

            

def testpy():
    custom_timedelta = timedelta(days=1)

    today = datetime.today()
    newsdate = datetime.strptime('2021.10.02 23:03', "%Y.%m.%d %H:%M")

    print(today)
    print(newsdate)
    diff = today - newsdate
    print(diff)
    print(diff <= custom_timedelta)
    print(diff >= custom_timedelta)

            

# testpy ()

fin = Finance_news()

fin.crawler('035720', 1, timedelta(days=1)) # 카카오
# fin.crawler('068270', 1, timedelta(days=1)) # 셀트리온
# fin.crawler('035420', 1, timedelta(days=1)) # 네이버

