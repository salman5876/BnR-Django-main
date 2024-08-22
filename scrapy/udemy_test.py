from scrapetools import *
import scrapy
from scrapy.crawler import CrawlerProcess

#request.meta['proxy'] = my_proxy
headers = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
my_proxy = getProxyWorking("https://www.udemy.com/",arr=True,strip=True,pcount=2)
proxy_array = my_proxy
my_proxy = proxy_array.pop()
pl = len(proxy_array)


class UdemySpider(scrapy.Spider):
    name = "udemy"

    custom_settings = {
        'CONCURRENT_REQUESTS': 300,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 150,
        'DOWNLOAD_DELAY': 0.1
    }

    def start_requests(self):
        urls = [
            'https://www.udemy.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,meta={"proxy":my_proxy},headers=headers)

    def parse(self, response):
        body = response.body
        index = getreIndex("navigation_categories\s*:\s*(\[)",body)
        cats_data = getJsonData(body[index:])
        urls_data = []
        count = 0
        for i in cats_data:
            cat = i["title"]
            for j in i["children"]:
                subcat = j["title"]
                url = getAbsUrl(response.url,j['absolute_url'])
                urls_data.append((cat,subcat,url,proxy_array[count%pl]))
                count+=1

        for current_cat,current_subcat,current_url,current_proxy in urls_data:
            yield scrapy.Request(url=current_url,callback=self.get_cat_id,meta={
                "proxy":current_proxy,
                "myprox":current_proxy,
                "cat": current_cat,
                "subcat" : current_subcat
            },headers=headers)

    def get_cat_id(self,response):
        cat = response.meta["cat"]
        subcat = response.meta["subcat"]
        proxy = response.meta["myprox"]
        body = response.body

        ind = getreIndex("UD.channel\s*=\s*({)",body)
        body = body[ind:]
        body = body[:body.index("};")+1]
        body = re.sub(".*==.*","",body)
        course_id = patSearch("id\D*(\d+)",body).group(1)

        data_url= "https://www.udemy.com/api-2.0/channels/{0}/courses?is_angular_app=true".format(course_id)


        yield scrapy.Request(url=data_url,callback=self.get_data,meta={
            "proxy":proxy,
            "myprox":proxy,
            "cat": cat,
            "subcat" : subcat
        },headers=headers,errback=self.err,priority=1)

    def err(self,fail):
        pass

    def get_data(self,response):
        cat = response.meta["cat"]
        subcat = response.meta["subcat"]
        proxy = response.meta["myprox"]

        current_data = json.loads(response.body)
        try:
            data_url = current_data["next"]
            yield scrapy.Request(url=data_url, callback=self.get_data, meta={
                "proxy": proxy,
                "myprox": proxy,
                "cat": cat,
                "subcat": subcat
            }, headers=headers, errback=self.err, priority=1)
        except:
            pass

        try:
            results = current_data["results"]

            for current_course in results:
                pass
        except:
            pass
        yield {}



process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(UdemySpider)

process.start()