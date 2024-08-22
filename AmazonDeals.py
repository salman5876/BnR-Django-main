import json
from time import sleep

from AmazonScrapeTools import ScrapeTools
import re

from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, TimeoutException


class AmazonDeals(ScrapeTools):
    def __init__(self):
        super(AmazonDeals,self).__init__(poolno=1)


    def scrape(self):
        n = 1
        while True:
            url = 'https://www.amazon.com/gp/goldbox/ref=gbps_ftr_s-5_5baf_page_{0}?gb_f_deals1=dealStates:AVAILABLE%252CWAITLIST%252CWAITLISTFULL%252CEXPIRED%252CSOLDOUT%252CUPCOMING,includedAccessTypes:,page:{1},sortOrder:BY_SCORE,dealsPerPage:48&pf_rd_p=a7e1c818-e7bc-4318-ae47-1f5300505baf&pf_rd_s=slot-5&pf_rd_t=701&pf_rd_i=gb_main&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=KEWRW1QF5F8S8GN1ANW2&ie=UTF8&nocache=1551270984190'.format(n, n)
            raw = self.getRawData(url=url)
            soup = self.getSoup(raw)

            products = soup.findAll('div',{'id':re.compile("^100_dealView_")})
            for i in products:
                try:
                    a = i.find('a',{'id': 'dealImage'})['href']
                    if 'page' in a:
                        pro_link = self.getAbsUrl(url,a)
                        raw_page = self.getRawData(url=pro_link)
                        soup_page = self.getSoup(raw_page)
                        links = soup_page.findAll('a',{'class':'oct-acs-asin-link'})
                        for i in links:
                            link = self.getAbsUrl(url,i['href'])
                            raww = self.getRawData(link)
                            soupp = self.getSoup(raww)
                            self.dealdata((self.scrape_data(soupp, link)))

                    else:
                        pro_link_p = self.getAbsUrl(url,a)
                        raw_page_p = self.getRawData(url=pro_link_p)
                        soup_page_p = self.getSoup(raw_page_p)
                        self.dealdata((self.scrape_data(soup_page_p, pro_link_p)))
                except Exception as e:
                    print (e)
            try:
                next_page = soup.find('div',{'id': 'FilterItemView_page_pagination'}).find('span',{'class':'a-declarative'})['data-gbfilter-pagination']
                dataaa = json.loads(next_page)
                m = dataaa['totalPages']
            except:
                break

            if m == n:
                break
            else:
                n += 1

    def scrape_data(self, soup, url):
        request = {}
        try:
            pattern = re.compile(r'ImageBlockATF', re.MULTILINE | re.DOTALL)
            img = soup.find("script", text=pattern)
            ImageText = []
            try:
                imgtext = re.search(r'initial(.*?)colorToAsin', img.string.strip(),flags=re.DOTALL | re.MULTILINE).group(1).strip()[3:-20]
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

            except:
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
            try:
                brand = soup.find("div", {"id": "bylineInfo_feature_div"}).find("a").find("img").text
                brand = soup.find("div", {"id": "bylineInfo_feature_div"}).find("a")['href'].split('/b', 1)[
                    0].strip('/')
            except:
                try:
                    brand = soup.find("div", {"id": "bylineInfo_feature_div"}).find("a").text.strip()
                except:
                    brand = soup.find("div", {"id": "merchant-info"}).find("a").text.strip()
            request["SNR_Brand"] = brand
            title = soup.find("span", {"id": "productTitle"}).text.strip()
            try:
                request["SNR_Title"] = title.encode('UTF-8')
            except:
                request["SNR_Title"] = str(title)
            try:
                Rating = soup.find("span", {"id": "acrPopover"})['title'].split(' out', 1)[0].strip()
            except:
                Rating = 0
            request["SNR_CustomerReviews"] = float(Rating)
            request["SNR_ProductURL"] = url
            try:
                PriceBefore = soup.find('span', {'class': 'a-text-strike'}).text.strip().split('$', 1)[
                    1]
                PriceBefore = [i.replace(',', '') for i in PriceBefore]
                PriceBefore = float(''.join(PriceBefore))
            except:
                PriceBefore = 0
            request["SNR_PriceBefore"] = PriceBefore
            try:
                Price = soup.find('span', {'id': 'priceblock_ourprice'}).text.strip().split('$', 1)[1]
                Price = [i.replace(',', '') for i in Price]
                Price = float(''.join(Price))
            except:
                try:
                    Price = soup.find('span', {'id': 'priceblock_ourprice'}).text.split('-', 1)[0].split('$',
                                                                                                         1)[
                        1].strip()
                    Price = [i.replace(',', '') for i in Price]
                    Price = float(''.join(Price))
                except:
                    try:
                        Price = soup.find('span', {
                            'class': 'a-size-base a-color-price a-color-price'}).text.strip().split('$', 1)[1]
                    except:
                        Price = 0
            request["SNR_PriceAfter"] = Price
            try:
                SKU = 'AZ' + soup.find('div', {'id': 'cerberus-data-metrics'})['data-asin']
            except:
                SKU = 'AZ' + soup.find('div', {'id': 'averageCustomerReviews'})['data-asin']
            request["SNR_SKU"] = SKU
            request["SNR_UPC"] = '00'
            request["SNR_Available"] = 'Amazon'
            request["SNR_Condition"] = 'New'
            try:
                Information = soup.findAll('th', {
                    'class': 'a-color-secondary a-size-base prodDetSectionEntry'})
                Information1 = soup.find('th', {
                    'class': 'a-color-secondary a-size-base prodDetSectionEntry'}).text
                for i in Information:
                    if i.text.strip().lower() == 'item model number':
                        ModelNo = i.parent.text.split('number', 1)[1].strip()
                        request["SNR_ModelNo"] = ModelNo
            except:
                try:
                    Information = soup.find('div', {'id': 'detailBullets_feature_div'})
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
                Description = soup.find('div', {'id': 'feature-bullets'}).find('ul')
                request["SNR_Description"] = str(Description)
            except:
                pass

            yield request


        except NoSuchElementException as e:
            print (e)

        except ElementNotVisibleException as r:
            print (r)

        except Exception as e:
            print (e)
            pass





if __name__ == '__main__':
    obj = AmazonDeals()
    obj.scrape()