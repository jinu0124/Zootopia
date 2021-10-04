from apscheduler.schedulers.asyncio import AsyncIOScheduler
from ..service.naver_finance_news_service import finance_news
from datetime import timedelta
class Scheduler:

    def __init__(self):
        self.sch = AsyncIOScheduler()
        self.sch.start()
        self.job_id = 'finance news'

        # 23:59(KST) -> 14:59 (UTC)
        # self.sch.add_job(self.getFinance, 'cron', hour=14, minute=59, second==10, max_instances=1)

        # 17:10(KST) -> 8:03 (UTC)
        self.sch.add_job(self.getFinance, 'cron', hour=17, minute=27, second=10, max_instances=1)
        # self.sch.add_job(self.getFinance, 'interval', seconds=20, max_instances=1)

    async def getFinance(self):

        kakao_df = finance_news.crawler('035720', 1, timedelta(days=1)) # 카카오
        # celltrion_df = finance_news.crawler('068270', 1, timedelta(days=1)) # 셀트리온
        # naver_df = finance_news.crawler('035420', 1, timedelta(days=1)) # 네이버

        print(kakao_df)
        # print(celltrion_df)
        # print(naver_df)



