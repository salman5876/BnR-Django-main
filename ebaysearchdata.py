import scrapy
from scrapy.crawler import CrawlerProcess


class BrickSetSpider(scrapy.Spider):
    name = 'veriz'
    allowed_domains = ['verizon.com']
    start_urls = ['https://www.verizonwireless.com/accessories/allproducts/']

    def parse(self, response):
        products_url = response.xpath('//*[@class="fontsz_sub2 bold color_red"]/a/@href').extract()
        for product in products_url:
            print "amad"
            print product
        # yield scrapy.Request(products_url, callback=self.parses, dont_filter=True)



        next_page = response.xpath('//*[@id="pageNav"]//a[2]/@href').extract_first()
        print next_page
        print "next page"

        absolute_next_page = response.urljoin(next_page)
        print absolute_next_page

        yield scrapy.Request(
            absolute_next_page,
            callback=self.parse,
            dont_filter=True
        )


    def parses(self, response):
        print response
        print "in parses mode"
        request = {}






process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(BrickSetSpider)

process.start()