from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leruamerlen.spiders.lm import LmSpider
from leruamerlen import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    # input = ('')
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LmSpider, search='перфоратор')

    process.start()