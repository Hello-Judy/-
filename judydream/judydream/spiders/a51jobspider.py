import scrapy


class A51jobspiderSpider(scrapy.Spider):
    # 每个项目的唯一名称，来区分不同的Spider
    name = "51jobspider"
    # 允许爬取的域名列表
    allowed_domains = ['yingjiesheng.com', 'www.yingjiesheng.com', 'q.yingjiesheng.com']
    
    # 起始URL列表 可以多个
    
    start_urls = [
        "https://q.yingjiesheng.com/pc/searchintern",
        "https://www.yingjiesheng.com/haigui/beijing/",
        "https://q.yingjiesheng.com/jobs/search/%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5?keywordType&jobarea=000000&pageCode=home%7Csearch%7Cjobsearchlb&funcCode=8044&isFromHomeKW=%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5"
        ]
    #  每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。
    #  该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象
    def parse(self, response):
        if "searchintern" in response.url:
            pass
        elif "haigui" in response.url:
            pass
        elif "%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5" in response.url:
            pass

    def parse_intern(self, response):
        print("This is intern page.")
        pass

    def parse_haigui(self, response):
        print("This is haigui page.")
        pass

    def parse_fulltime(self, response):
        print("This is fulltime page.")
        second_page_link = response.css('#list .search-list-href a::attr(href)').getall()
        print(f"How many {len(second_page_link)} elements found on the page.!!!")



