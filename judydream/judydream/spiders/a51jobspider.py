import scrapy


class A51jobspiderSpider(scrapy.Spider):
    # 每个项目的唯一名称，来区分不同的Spider
    name = "51jobspider"
    # 允许爬取的域名列表
    allowed_domains = ["51job.com"]
    # 起始URL列表
    start_urls = ["https://51job.com"]
    #  每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    #  该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象
    def parse(self, response):
        pass
