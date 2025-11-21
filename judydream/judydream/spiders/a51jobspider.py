import scrapy
import re

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
            self.parse_intern(response)
        elif "haigui" in response.url:
            self.parse_haigui(response)

        elif "%E6%95%B0%E6%8D%AE%E8%BF%90%E8%90%A5" in response.url:
            # 把子解析函数产生的 Request 交回给引擎
            yield from self.parse_fulltime(response)

    def parse_intern(self, response):
        print("This is intern page.")
        pass

    def parse_haigui(self, response):
        print("This is haigui page.")
        pass


    

    def parse_fulltime(self, response):
        print("This is fulltime page.")
        get_link = response.css('#list .search-list-href[data-v-73d24bfa]::attr(href)').getall()
        print("type of link:", type(get_link))
        print(f"在一级页面找到 {len(get_link)} 个职位链接")
        # 遍历一级页面的每一个职位的链接
        for link in get_link:
            # 处理链接，去掉参数部分
            #link = link.split('?')[0]  
            link = response.urljoin(link)
            print("Processed second URL:", link)

            # 创建二级页面的请求，并指定回调函数为 parse_job_detail
            yield scrapy.Request(url=link, 
                                 callback=self.parse_job_detail
                                )  
            
    def parse_job_detail(self, response):
        item = {}

        item['job_title'] = response.css('#detail .jobtitle .detail-title-left-top .job[data-v-1bc90c70]::text').get()
        item['job_description'] = response.css('#detail .detail-content-common .text[data-v-1bc90c70]:last-child::text').get()
        item['company_name'] = response.css('#detail .detail-content-compnav-center span[data-v-1bc90c70]::text').get()
        item['posting_date'] = response.css('#detail .jobtitle .detail-title-left-center .time[data-v-1bc90c70]::text').get().strip()
        pattern = r"^\D+"
        new_posting_date = re.sub(pattern, "", item['posting_date'])
        item['posting_date'] = new_posting_date
        item["Type"] = "Full-time"
        item['application_link'] = response.url
        
        print("Application Link:", item['application_link'])




    
  
