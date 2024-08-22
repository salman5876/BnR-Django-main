from multiprocessing.pool import ThreadPool
import requests
from ScrapeTools import ScrapeTools
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
import bottlenose
import json
import xmltodict
from multiprocessing import Pool
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import re
from bs4 import BeautifulSoup

# def unwrap_self_f(arg, **kwarg):
#     return Products.Data_Scraper(*arg, **kwarg)

class Products(ScrapeTools):
    textFile = 'AmazonBoy.txt'
    def __init__(self):
        super(Products,self).__init__(poolno=1)

    def appendLog(self,data):  #############  Appending URLs in File #############
        try:
            open(self.textFile, "w").close()
            with open(self.textFile, "a") as w:
                for i in data:
                    w.writelines(','.join(i) + '\n')
                print data
        except Exception as e:
            print e

    def get_data_Textfile(self):
        data = []
        with open(self.textFile, 'r') as f:

            data = [i.split(',') for i in f]
            for index, j in enumerate(data):
                j[len(j) - 1] = j[len(j) - 1][:-1]
            print data
            data1 = data

            # try:
            #     with open("testinggg.txt", "a") as w:
            #         for k in data:
            #             w.write('\''+k[0] + ',' + ','.join(k[1:-1]) + '\':' + ' [],' + "\n")
            # except Exception as e:
            #     pass

            # driver1 = self.getWebDriver()
            # driver2 = self.getWebDriver()
            # verts = [None] * self.poolno
            # for i in range(0,self.poolno):
            #     verts[i] = requests.Session()
            # c=0
            # for index,item in enumerate(data):
            #     if index % self.poolno == 0:
            #         c=0
            #     item.append(verts[c])
            #     c = c+1

            # pool = ThreadPool(2)
            # results = pool.map(unwrap_self_f, zip([self]*len(data), data))
            # pool.close()
            # pool.join()

            # p = Pool(self.poolno)
            #
            # result = p.map(unwrap_self_f, zip([self]*len(data), data))
            for index,k in enumerate(data):
                data1 = data1[1:] + data1[:1]
                self.appendLog(data1)
                self.Data_Scraper(k)
                # self.appendLog(','.join((data[index][0],data[index][1],data[index][2])).encode('utf-8').strip())
            print 'Completed'
            return data

    def find(self,key, dictionary):
        if isinstance(dictionary, dict):
            for k, v in dictionary.items():
                if k == key:
                    yield v
                elif isinstance(v, dict):
                    for result in self.find(key, v):
                        yield result
                elif isinstance(v, list):
                    for d in v:
                        for result in self.find(key, d):
                            yield result

    def scrape_data(self,soup, url):
        item_list = []
        response_stat = "<?xml version=\"1.0\" ?><ItemLookupResponse xmlns=\"http://webservices.amazon.com/AWSECommerceService/2013-08-01\">"
        is_next = True
        n = 0
        robot = 'automated access'
        count = 0
        while is_next:
            n +=1
            is_next = False
            try:
                items_div = soup.select("ul.s-result-list li[id*=result] div.s-item-container")
                print items_div[0]
            except:
                if soup:
                    items_div = soup.select("div.s-result-item span.rush-component a.a-link-normal")
                else:
                    break
            for current_item_div in items_div:
                request = {}
                try:


                    # request["SNR_SKU"] = "AZ" + current_item_div.parent["data-asin"]
                    #
                    # image_div = current_item_div.select_one("img.s-access-image")
                    #
                    # try:
                    #     temp = re.split(",\s+", image_div["srcset"])[-1]
                    #     request["SNR_ImageURL"] = temp.split(" ")[0].strip()
                    # except:
                    #     request["SNR_ImageURL"] = image_div["src"]
                    # request["SNR_ModelNo"] = "00"
                    # request["SNR_UPC"] = "00"
                    # request["SNR_Available"] = "Amazon"
                    # request["SNR_Description"] = "Visit site to see description"
                    # request["SNR_Title"] = image_div["alt"]
                    # link_div = current_item_div.select_one("a.s-access-detail-page")
                    #
                    # request["SNR_ProductURL"] = self.getAbsUrl(url, link_div["href"])
                    #
                    # request["SNR_Condition"] = "00"
                    # item_raw = str(current_item_div)
                    # try:
                    #     temp = self.patSearch("Suggested\s+[^\$]+\$([\d\.,]+)", item_raw).group(1).replace(",", "")
                    #     request["SNR_PriceBefore"] = float(temp)
                    # except:
                    #     request["SNR_PriceBefore"] = -1
                    #
                    # try:
                    #     request["SNR_CustomerReviews"] = float(
                    #         current_item_div.select_one("i[class*=a-star] span.a-icon-alt").text.strip().split(
                    #             "out of")[0].strip()
                    #     )
                    # except:
                    #     request["SNR_CustomerReviews"] = 0.0
                    #
                    #
                    # brand = "No Brand"
                    #
                    # try:
                    #     temp = self.patSearch("by\s+</span><span[^>]+>(\w+)<", item_raw).group(1)
                    #     brand = temp
                    # except:
                    #     pass
                    #
                    # request["SNR_Brand"] = brand
                    # price_div = current_item_div.select_one("span.sx-price")
                    # try:
                    #     price = price_div.select_one("span.sx-price-whole").text.strip()
                    #
                    #     try:
                    #         temp = ".%s" % price_div.select_one("sup.sx-price-fractional").text.strip()
                    #         price += temp
                    #     except Exception as e:
                    #         pass
                    #
                    # except:
                    #     try:
                    #         price = self.patSearch('a-color-base">\$([\.\d\,]+)', item_raw).group(1)
                    #     except:
                    #         temp = current_item_div("span.acs_product-price__buying").text.strip()
                    #         price = 0.0
                    #         if temp:
                    #             try:
                    #                 price = self.patSearch("\$([\d\.,]+)", temp).group(1)
                    #             except:
                    #                 if "FREE" not in temp:
                    #                     continue
                    #
                    # request["SNR_Price"] = float(price.replace(",", ""))
                    try:
                        link_div = current_item_div.select_one("a.s-access-detail-page")
                        pro_url = self.getAbsUrl(url, link_div["href"])
                    except:
                        # link_div = current_item_div['href']
                        pro_url = self.getAbsUrl(url, current_item_div["href"])

                    # rawdata = self.getRawData(pro_url,session=sess)
                    while True:
                        try:
                            print 'sel data From {0}'.format(pro_url)
                            self.driver.get(pro_url)
                            # rawdata,sess = self.getRawData(pro_url, session=sess)

                            if count >= 200:
                                print '200 Count Complete'
                                self.driver.quit()
                                self.display.stop()
                                self.proxy = self.getProxyWorking(ur = pro_url)
                                # driver = self.getWebDriver(proxy=self.proxy)
                                # self.driver = self.getWebDriver()
                                count = 0
                                continue

                            # if count >= 200:
                            #     sess.close()
                            #     self.proxy = self.getProxyWorking(ur = pro_url)
                            #     sess = requests.Session()
                            #     count = 0
                            #     continue


                            if robot in self.driver.page_source:
                                print 'Robot'
                                self.driver.quit()
                                self.display.stop()
                                # sleep(300)/
                                self.proxy = self.getProxyWorking(ur=pro_url)
                                # driver = self.getWebDriver(proxy=self.proxy)
                                # self.driver = self.getWebDriver()

                                continue
                            else:
                                count += 1
                                # sleep(5)
                                break

                        except TimeoutException:
                            print 'Timeout'
                            self.driver.quit()
                            self.display.stop()
                            self.proxy = self.getProxyWorking(ur=pro_url)
                            # driver = self.getWebDriver(proxy=self.proxy)
                            # self.driver = self.getWebDriver()
                            continue
                        except Exception as e:
                            print e
                            # sleep(300)
                            self.driver.quit()
                            self.display.stop()
                            self.proxy = self.getProxyWorking(ur=pro_url)
                    #
                    # button = driver.find_elements_by_css_selector(".a-button.a-button-thumbnail.a-button-toggle")
                    # for data in button:
                    #     hover = ActionChains(driver).move_to_element(data)
                    #     hover.perform()
                    #     driver.implicitly_wait(10)
                    soup_pro = BeautifulSoup(self.driver.page_source, "lxml")
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
                        brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").find("img").text
                        brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a")['href'].split('/b', 1)[
                            0].strip('/')
                    except:
                        try:
                            brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").text.strip()
                        except:
                            brand = soup_pro.find("div", {"id": "merchant-info"}).find("a").text.strip()
                    request["SNR_Brand"] = brand
                    title = soup_pro.find("span", {"id": "productTitle"}).text.strip()
                    try:
                        request["SNR_Title"] = title.encode('UTF-8')
                    except:
                        request["SNR_Title"] = str(title)
                    try:
                        Rating = soup_pro.find("span", {"id": "acrPopover"})['title'].split(' out', 1)[0].strip()
                    except:
                        Rating = 0
                    request["SNR_CustomerReviews"] = float(Rating)
                    request["SNR_ProductURL"] = pro_url
                    try:
                        PriceBefore = soup_pro.find('span', {'class': 'a-text-strike'}).text.strip().split('$', 1)[
                            1]
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
                            Price = \
                                soup_pro.find('span', {'id': 'priceblock_ourprice'}).text.split('-', 1)[0].split('$',
                                                                                                                 1)[
                                    1].strip()
                            Price = [i.replace(',', '') for i in Price]
                            Price = float(''.join(Price))
                        except:
                            try:
                                Price = soup_pro.find('span', {
                                    'class': 'a-size-base a-color-price a-color-price'}).text.strip().split('$', 1)[1]
                            except:
                                Price = 0
                    request["SNR_Price"] = Price
                    try:
                        SKU = 'AZ' + soup_pro.find('div', {'id': 'cerberus-data-metrics'})['data-asin']
                    except:
                        SKU = 'AZ' + soup_pro.find('div', {'id': 'averageCustomerReviews'})['data-asin']
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
                        request["SNR_Description"] = str(Description)
                    except:
                        pass



                    # asin = current_item_div.parent["data-asin"]
                    # amazon = bottlenose.Amazon('AKIAJYH5LPTVAMBU6NOQ', 'DfGaLxsy9ftS/672f0VxCWgoXecj3LRxNoqLMNPA','mobilea0fe6ba-20')
                    # while True:
                    #     response = amazon.ItemLookup(ItemId=asin,ResponseGroup='Accessories,BrowseNodes,EditorialReview,Images,ItemAttributes,ItemIds,Large,Medium,OfferFull,Offers,PromotionSummary,OfferSummary,RelatedItems,Reviews,SalesRank,Similarities,Small,Tracks,VariationImages')
                    #     if response_stat in response:
                    #         count = count + 1
                    #         print 'count outside', count
                    #         print 'ASIN', asin
                    #         sleep(1)
                    #         # print 'ASIN is', asin
                    #         break
                    # response = json.dumps(xmltodict.parse(response), indent=4)
                    # response = json.loads(response)
                    # data_dict = response['ItemLookupResponse']['Items']['Item']
                    # images = ''
                    # try:
                    #     for index, j in enumerate(self.find('HiResImage', data_dict)):
                    #         if index == 0:
                    #             images = j['URL']
                    #         elif index >= 6:
                    #             break
                    #         else:
                    #             images = images + ',' + j['URL']
                    #     if images == '':
                    #         image_div = current_item_div.select_one("img.s-access-image")
                    #
                    #         try:
                    #             temp = re.split(",\s+", image_div["srcset"])[-1]
                    #             images = temp.split(" ")[0].strip()
                    #         except:
                    #             images = image_div["src"]
                    # except:
                    #     image_div = current_item_div.select_one("img.s-access-image")
                    #
                    #     try:
                    #         temp = re.split(",\s+", image_div["srcset"])[-1]
                    #         images = temp.split(" ")[0].strip()
                    #     except:
                    #         images = image_div["src"]
                    # request["SNR_ImageURL"] = images
                    # request["SNR_Brand"] = data_dict['ItemAttributes']['Brand']
                    # request["SNR_Title"] = data_dict['ItemAttributes']['Title']
                    # request["SNR_ProductURL"] = data_dict['DetailPageURL']
                    # request["SNR_SKU"] = 'AZ' + data_dict['ASIN']
                    # request["SNR_Available"] = 'Amazon'
                    # try:
                    #     request["SNR_Description"] = str(data_dict['ItemAttributes']['Feature'])
                    # except:
                    #     for index, item in enumerate(self.find('ItemLink', data_dict)):
                    #         if index == 0:
                    #             request["SNR_Description"] = str(item)
                    #         else:
                    #             break
                    # try:
                    #     request["SNR_PriceBefore"] = float(
                    #         data_dict['ItemAttributes']['ListPrice']['FormattedPrice'].split('$')[1])
                    # except:
                    #     request["SNR_PriceBefore"] = 00
                    # try:
                    #     request["SNR_CustomerReviews"] = float(current_item_div.select_one("i[class*=a-star] span.a-icon-alt").text.strip().split("out of")[0].strip())
                    # except:
                    #     request["SNR_CustomerReviews"] = 0.0
                    # try:
                    #     request["SNR_ModelNo"] = data_dict['ItemAttributes']['Model']
                    # except:
                    #     request["SNR_ModelNo"] = '00'
                    # try:
                    #     request["SNR_UPC"] = data_dict['ItemAttributes']['UPC']
                    # except:
                    #     request["SNR_UPC"] = '00'
                    # try:
                    #     for index, item in enumerate(self.find('Price', data_dict)):
                    #         if index == 0:
                    #             request["SNR_Price"] = float(item['FormattedPrice'].split('$')[1])
                    #         else:
                    #             break
                    # except:
                    #     try:
                    #         for index, item in enumerate(self.find('LowestNewPrice', data_dict)):
                    #             if index == 0:
                    #                 request["SNR_Price"] = float(item['FormattedPrice'].split('$')[1])
                    #             else:
                    #                 break
                    #     except:
                    #         item_raw = str(current_item_div)
                    #         price_div = current_item_div.select_one("span.sx-price")
                    #         try:
                    #             price = price_div.select_one("span.sx-price-whole").text.strip()
                    #
                    #             try:
                    #                 temp = ".%s" % price_div.select_one("sup.sx-price-fractional").text.strip()
                    #                 price += temp
                    #             except Exception as e:
                    #                 pass
                    #
                    #         except:
                    #             try:
                    #                 price = self.patSearch('a-color-base">\$([\.\d\,]+)', item_raw).group(1)
                    #             except:
                    #                 temp = current_item_div("span.acs_product-price__buying").text.strip()
                    #                 price = 0.0
                    #                 if temp:
                    #                     try:
                    #                         price = self.patSearch("\$([\d\.,]+)", temp).group(1)
                    #                     except:
                    #                         if "FREE" not in temp:
                    #                             continue
                    #
                    #         request["SNR_Price"] = float(price.replace(",", ""))
                    #
                    # try:
                    #     for index, item in enumerate(self.find('Condition', data_dict)):
                    #         if index == 0:
                    #             request["SNR_Condition"] = item
                    #         else:
                    #             break
                    # except:
                    #     request["SNR_Condition"] = '00'

                    # for key, value in data_dict['ImageSets'].items():
                    #     for i in range(0, len(value)):
                    #         if i == 0:
                    #             images = value[i]['HiResImage']['URL']
                    #         else:
                    #             images = images + ',' + value[i]['HiResImage']['URL']
                    # request["SNR_ImageURL"] = images
                    # request["SNR_Brand"] = data_dict['ItemAttributes']['Brand']
                    # request["SNR_Title"] = data_dict['ItemAttributes']['Title']
                    # request["SNR_ProductURL"] = data_dict['DetailPageURL']
                    # request["SNR_SKU"] = 'AZ' + data_dict['ASIN']
                    # request["SNR_Available"] = 'Amazon'
                    # request["SNR_Description"] = str(data_dict['ItemAttributes']['Feature'])
                    # try:
                    #     request["SNR_PriceBefore"] = float(data_dict['ItemAttributes']['ListPrice']['FormattedPrice'].split('$')[1])
                    # except:
                    #     request["SNR_PriceBefore"] = 00
                    # try:
                    #     request["SNR_CustomerReviews"] = float(current_item_div.select_one("i[class*=a-star] span.a-icon-alt").text.strip().split("out of")[0].strip())
                    # except:
                    #     request["SNR_CustomerReviews"] = 0.0
                    # try:
                    #     request["SNR_ModelNo"] = data_dict['ItemAttributes']['Model']
                    # except:
                    #     request["SNR_ModelNo"] = '00'
                    # try:
                    #     request["SNR_UPC"] = data_dict['ItemAttributes']['UPC']
                    # except:
                    #     request["SNR_UPC"] = '00'
                    # try:
                    #     request["SNR_Price"] = float(self.getkey(self.find('Price',data_dict))['FormattedPrice'].split('$')[1])
                    # except:
                    #     try:
                    #         request["SNR_Price"] = float(self.getkey(self.find('LowestNewPrice', data_dict))['FormattedPrice'].split('$')[1])
                    #     except:
                    #         item_raw = str(current_item_div)
                    #         price_div = current_item_div.select_one("span.sx-price")
                    #         try:
                    #             price = price_div.select_one("span.sx-price-whole").text.strip()
                    #
                    #             try:
                    #                 temp = ".%s" % price_div.select_one("sup.sx-price-fractional").text.strip()
                    #                 price += temp
                    #             except Exception as e:
                    #                 pass
                    #
                    #         except:
                    #             try:
                    #                 price = self.patSearch('a-color-base">\$([\.\d\,]+)', item_raw).group(1)
                    #             except:
                    #                 temp = current_item_div("span.acs_product-price__buying").text.strip()
                    #                 price = 0.0
                    #                 if temp:
                    #                     try:
                    #                         price = self.patSearch("\$([\d\.,]+)", temp).group(1)
                    #                     except:
                    #                         if "FREE" not in temp:
                    #                             continue
                    #
                    #         request["SNR_Price"] = float(price.replace(",", ""))
                    # try:
                    #     request["SNR_Condition"] = self.getkey(self.find('Condition', data_dict))
                    # except:
                    #     request["SNR_Condition"] = '00'

                    yield request


                except NoSuchElementException as e:
                    print e

                except ElementNotVisibleException as r:
                    print r

                except Exception as e:
                    print e
                    pass

            if n == 10:
                # sess.close()
                self.driver.quit()
                self.display.stop()
                break

            try:
                next_div = soup.select_one("a#pagnNextLink")["href"]
            except:
                try:
                    next_div = soup.select_one("li.a-last a")["href"]
                except:
                    break


            if next_div:
                url = self.getAbsUrl(url, next_div)
                # ProxyTimeTest()
                raw = self.getRawData(url)
                if raw == None:
                    continue
                if "did not match any products" not in raw:
                    soup = self.getSoup(raw)
                    soup = self.get_post_soup(soup)
                    is_next = True
            else:
                break

    def get_data_all(self,dt, cat, subcat):
        for request in dt:
            request["SNR_Category"] = cat
            request["SNR_SubCategory"] = subcat
            yield request

    def get_post_soup(self,soup):
        temp = soup.select_one("div#rightResultsATF")
        if not temp:
            temp = soup.select_one("div[id*=search-results]")
        if not temp:
            temp = soup.select_one("div.s-right-column")

        return temp

    def Data_Scraper(self,data):
        cat,subcat,url_link = data
        print ','.join(data[1:-1])
        # ProxyTimeTest()
        raw = self.getRawData(url_link)
        if raw == None:
            return 'no'
        soup = self.getSoup(raw)
        # driver = self.getWebDriver(proxy=self.proxy)
        post_soup = self.get_post_soup(soup)
        # self.scrape_data(post_soup, url_link,sess,driver)
        self.commit_data(self.get_data_all(self.scrape_data(post_soup, url_link), cat, subcat),batch_size=500)

# drivers = getWebDriver()

def main():
    blu = Products()
    blu.get_data_Textfile()


if __name__ == '__main__':
    main()