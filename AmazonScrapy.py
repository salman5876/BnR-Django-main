import re
import json
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer, DailyDeals_Serializer,AmazonURLs_Serializer
from products.models import AmazonURLs, AllProducts, AmazonProxies


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011',
            'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011',
            'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011',
            'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011',
            'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011',
            'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011',
        ]
        proo = AmazonProxies.objects.order_by('count')[0]
        proxy = proo.proxy
        proo.count += 1
        proo.save()
        objesc = AllProducts.objects.all()[:100]
        meta_proxy = "http://{0}".format(proxy)
        for url in objesc:
            yield scrapy.Request(url=url.SNR_ProductURL, callback=self.parse,errback=self.errback_httpbin, meta={'proxy': meta_proxy},dont_filter=True)

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)
            proo = AmazonProxies.objects.order_by('count')[0]
            proxy = proo.proxy
            proo.count += 1
            proo.save()
            meta_proxy = "http://{0}".format(proxy)
            yield scrapy.Request(url=response.url, callback=self.parse, errback=self.errback_httpbin,meta={'proxy': meta_proxy}, dont_filter=True)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)


    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
        request = {}
        try:
            if 'automated access' in str(response.body):
                print 'Robot'
                proo = AmazonProxies.objects.order_by('count')[0]
                proxy = proo.proxy
                proo.count += 1
                proo.save()
                meta_proxy = "http://{0}".format(proxy)
                yield scrapy.Request(url=response.url, callback=self.parse, errback=self.errback_httpbin,meta={'proxy': meta_proxy}, dont_filter=True)

            soup_pro = BeautifulSoup(response.body, "lxml")
            pattern = re.compile(r'ImageBlockATF', re.MULTILINE | re.DOTALL)
            img = soup_pro.find("script", text=pattern)
            ImageText = []
            try:
                imgtext = re.search(r'initial(.*?)colorToAsin', img.string.strip(),
                                    flags=re.DOTALL | re.MULTILINE).group(1).strip()[3:-20]
                dataaa = json.loads(imgtext)
                for index, i in enumerate(dataaa):
                    if index == 0:
                        ImageText.append(i['hiRes'])
                        if ImageText[index] == None:
                            ImageText.pop()
                            ImageText.append(i['large'])
                            if ImageText[index] == None:
                                ImageText.pop()
                                ImageText.append(i['lowRes'])
                    else:
                        ImageText.append(i['hiRes'])
                        if ImageText[index] == None:
                            ImageText.pop()
                            ImageText.append(i['large'])
                            if ImageText[index] == None:
                                ImageText.pop()
                                ImageText.append(i['lowRes'])
                request["SNR_ImageURL"] = ','.join(ImageText)

            except:
                try:
                    imgtext = re.search(r'imageGalleryData(.*?)centerColMargin', img.string.strip(),
                                        flags=re.DOTALL | re.MULTILINE).group(1).strip()[3:-11]
                    dataaa = json.loads(imgtext)
                    for index, i in enumerate(dataaa):
                        if index == 0:
                            ImageText.append(i['mainUrl'])
                            if ImageText[index] == None:
                                ImageText.append(i['thumbUrl'])
                        else:
                            ImageText.append(i['mainUrl'])
                            if ImageText[index] == None:
                                ImageText.append(i['thumbUrl'])
                    request["SNR_ImageURL"] = ','.join(ImageText)
                except:
                    ImageText = None
            if request["SNR_ImageURL"] == None or request["SNR_ImageURL"] == '':
                try:
                    ImageText = soup_pro.find("img", {'id': 'imgBlkFront'})['src']
                except:
                    ImageText = None
                if ImageText == None or ImageText == '':
                    try:
                        ImageText = soup_pro.find("img", {'id': 'fine-art-landingImage'})['src']
                    except:
                        ImageText = None
                if ImageText == None or ImageText == '':
                    try:
                        ImageText = soup_pro.findAll("div", {'class', 'av-bgimg__div'})[0]['style']
                        ImageText = re.search(r'\((.*?)\)', ImageText, flags=re.DOTALL | re.MULTILINE).group(
                            1).strip()
                    except:
                        ImageText = None
                if ImageText == None or ImageText == '':
                    try:
                        ImageText = soup_pro.find('div', {'class': 'av-fallback-packshot'}).find('img')['src']
                    except:
                        ImageText = None
                if ImageText == None or ImageText == '':
                    try:
                        ImageText = soup_pro.find('div', {'id': 'img-canvas'}).find('img')['src']
                    except:
                        ImageText = None
                request["SNR_ImageURL"] = ImageText

            try:
                brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").find(
                    "img").text.strip()
            except:
                brand = None
            if brand == None or brand == '':
                try:
                    brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").text.strip()
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    brand = \
                        soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a")['href'].split('/b', 1)[
                            0].strip(
                            '/')
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    brand = soup_pro.find("div", {"id": "merchant-info"}).find("a").text.strip()
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    brand = soup_pro.find("div", {'id': 'brandBylineWrapper'}).find('a').text.strip()
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    brand = soup_pro.find("div", {'id': 'brandBarLogoWrapper'}).find('img')['alt']
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    brand = soup_pro.find("a", {'id': 'fine-ART-ProductLabelArtistNameLink'}).text.strip()
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    pat = re.compile(r'Studio', re.MULTILINE | re.DOTALL)
                    brand = soup_pro.find('th', text=pat).find_next_sibling().text.strip()
                except:
                    brand = None
            if brand == None or brand == '':
                try:
                    pat = re.compile(r'Studio', re.MULTILINE | re.DOTALL)
                    brand = soup_pro.find('span', text=pat).find_parent().find_next_sibling().text.strip()
                except:
                    brand = '00'
            request["SNR_Brand"] = brand
            try:
                title = soup_pro.find("span", {"id": "productTitle"}).text.strip()
            except:
                title = None
            if title == None:
                try:
                    title = soup_pro.find("span", {'id': 'ebooksProductTitle'}).text.strip()
                except:
                    title = None
            if title == None:
                try:
                    title = soup_pro.find("div", {'id': 'mnbaProductTitleAndYear'}).text.strip()
                except:
                    title = None
            if title == None:
                try:
                    title = soup_pro.find('h1', {'data-automation-id': 'title'}).text.strip()
                except:
                    title = '00'
            try:
                request["SNR_Title"] = title.encode('UTF-8')
            except:
                request["SNR_Title"] = str(title)
            try:
                Rating = soup_pro.find("span", {"id": "acrPopover"})['title'].split(' out', 1)[0].strip()
            except:
                try:
                    Rating = \
                    soup_pro.find("span", {"class": "arp-rating-out-of-text a-color-base"}).text.split(' out', 1)[
                        0].strip()
                except:
                    Rating = 0
            request["SNR_CustomerReviews"] = float(Rating)
            request["SNR_ProductURL"] = response.url
            try:
                PriceBefore = soup_pro.find('span', {'class': 'a-text-strike'}).text.strip().split('$', 1)[1]
                PriceBefore = [i.replace(',', '') for i in PriceBefore]
                PriceBefore = float(''.join(PriceBefore))
            except:
                PriceBefore = 0
            request["SNR_PriceBefore"] = PriceBefore
            try:
                Price = soup_pro.find('span', {'id': 'priceblock_ourprice'}).text.strip().split('$', 1)[1]
                Price = [i.replace(',', '') for i in Price]
                Price = float(''.join(Price))
            except:
                try:
                    Price = soup_pro.find('span', {'id': 'priceblock_ourprice'}).text.split('-', 1)[0].split('$', 1)[
                        1].strip()
                    Price = [i.replace(',', '') for i in Price]
                    Price = float(''.join(Price))
                except:
                    try:
                        Price = soup_pro.find('span', {
                            'class': 'a-size-base a-color-price a-color-price'}).text.strip().split('$', 1)[1]
                    except:
                        Price = 0
            if Price == 0:
                try:
                    pat = re.compile(r'HD', re.MULTILINE | re.DOTALL)
                    Price = soup_pro.findAll('strong', text=pat)
                    if len(Price) > 1:
                        Price = Price[1].find_parent().text.strip().split('$', 1)[1]
                    else:
                        Price = Price[0].find_parent().text.strip().split('$', 1)[1]
                except:
                    Price = 0
            request["SNR_Price"] = Price
            pattern = re.compile(r'ASIN:', re.MULTILINE | re.DOTALL)
            try:
                SKU = 'AZ' + soup_pro.find('div', {'id': 'cerberus-data-metrics'})['data-asin']
            except:
                SKU = None
            if SKU == None:
                try:
                    SKU = 'AZ' + soup_pro.find('div', {'id': 'averageCustomerReviews'})['data-asin']
                except:
                    SKU = None
            if SKU == None:
                try:
                    SKU = 'AZ' + soup_pro.find("span", text=pattern).find_next_sibling("span").text.strip()
                except:
                    SKU = None
            if SKU == None:
                try:
                    pat = re.compile(r'HD', re.MULTILINE | re.DOTALL)
                    SKU = soup_pro.find('strong', text=pat)
                    SKU = "AZ" + SKU.find_parent()['data-asin']
                except:
                    SKU = None
            if SKU == None:
                try:
                    SKU = 'AZ' + soup_pro.find("input", {'id': 'ASIN'})['value']
                except:
                    SKU = None
            request["SNR_SKU"] = SKU
            request["SNR_UPC"] = '00'
            request["SNR_Available"] = 'Amazon'
            request["SNR_Condition"] = 'New'
            try:
                Information = soup_pro.findAll('th', {
                    'class': 'a-color-secondary a-size-base prodDetSectionEntry'})
                Information1 = soup_pro.find('th', {
                    'class': 'a-color-secondary a-size-base prodDetSectionEntry'}).text
                for i in Information:
                    if i.text.strip().lower() == 'item model number':
                        ModelNo = i.parent.text.split('number', 1)[1].strip()
                        request["SNR_ModelNo"] = ModelNo
            except:
                try:
                    Information = soup_pro.find('div', {'id': 'detailBullets_feature_div'})
                    Information = Information.findAll('span', {'class': 'a-text-bold'})
                    for i in Information:
                        if i.text.strip().lower() == 'item model number:':
                            ModelNo = i.parent.text.split('number:', 1)[1].strip()
                            request["SNR_ModelNo"] = ModelNo
                        else:
                            request["SNR_ModelNo"] = '00'
                except:
                    request["SNR_ModelNo"] = '00'

            try:
                Description = soup_pro.find('div', {'id': 'feature-bullets'}).find('ul')
            except:
                Description = None
            if Description == None:
                try:
                    Description = soup_pro.find('table', {'class', 'product-details-meta'})
                except:
                    Description = None
            if Description == None:
                try:
                    Description = soup_pro.find('div', {'class', '_2Lb-Sl'})
                except:
                    Description = None
            if Description == None:
                try:
                    pat = re.compile(r'Product details', re.MULTILINE | re.DOTALL)
                    Description = soup_pro.find('h2', text=pat).find_next_sibling()
                except:
                    Description = None
            request["SNR_Description"] = str(Description)
            print request

        except Exception as e:
            print e
            pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'
    })

process.crawl(QuotesSpider)

process.start()