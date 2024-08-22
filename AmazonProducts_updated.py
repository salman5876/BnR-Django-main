from multiprocessing.pool import ThreadPool
import requests
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer, DailyDeals_Serializer,AmazonURLs_Serializer
from products.models import AmazonURLs, AllProducts, AmazonProxies
from django.db.models.query_utils import Q
from AmazonScraptools_updated import ScrapeTools
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
#     return Products.scrape_data(*arg, **kwarg)

class Products(ScrapeTools):
    def __init__(self):
        super(Products,self).__init__(poolno=1)

    def appendLog(self,data):  #############  Appending URLs in File #############
        try:
            open(self.textFile, "w").close()
            with open(self.textFile, "a") as w:
                for i in data:
                    w.writelines(','.join(i) + '\n')
                print(data)
        except Exception as e:
            print(e)

    def get_data_Textfile(self):
        data1=[]
        data = self.getScrapeData()

        for item in data:
            data1.append({'cat':item['Cat'],'subcat':item['SubCat'],'url':item['url']})

            # try:
            #     with open("testinggg.txt", "a") as w:
            #         for k in data:
            #             w.write('\''+k[0] + ',' + ','.join(k[1:-1]) + '\':' + ' [],' + "\n")
            # except Exception as e:
            #     pass

        # p = Pool(self.poolno)
        # result = p.map(unwrap_self_f, zip([self]*len(data1), data1))
        # p.close()
        # p.join()

        for index, k in enumerate(data1):
            self.scrape_data(k)
            self.changeStatus(k)
            # data1 = data1[1:] + data1[:1]
            # self.appendLog(data1)
            # self.appendLog(','.join((data[index][0],data[index][1],data[index][2])).encode('utf-8').strip())
        print('Completed')
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

    def individulaProduct(self,dic):
        request = {}
        count = 0
        robot = 'automated access'
        pro_url = dic['url']
        driver = dic['driver']
        cat = dic['cat']
        subcat = dic['subcat']
        while True:
            try:
                print('Product data From {0}'.format(pro_url))
                driver.get(pro_url)
                if robot in driver.page_source:
                    print('Robot')
                    return 'Robot'
                if 'images-na.ssl-images-amazon.com' not in driver.page_source:
                    print('Loading')
                    return 'Loading'
                break

            except TimeoutException:
                print('Timeout')
                return 'Timeout'
            except Exception as e:
                print('Connection Refused')
                return 'Connection'

        soup_pro = BeautifulSoup(driver.page_source, "lxml")
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
                    soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a")['href'].split('/b', 1)[0].strip(
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
                Rating = soup_pro.find("span", {"class": "arp-rating-out-of-text a-color-base"}).text.split(' out', 1)[
                    0].strip()
            except:
                Rating = 0
        request["SNR_CustomerReviews"] = float(Rating)
        request["SNR_ProductURL"] = pro_url
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
        request["SNR_Category"] = cat
        request["SNR_SubCategory"] = subcat

        self.commit_data(request)
        # return request
    def getMainPage(self,data):
        robot = 'automated access'
        url_link = data['url']
        driver = data['driver']
        while True:
            try:
                print('Cat_page data From {0}'.format(url_link))
                driver.get(url_link)
                if robot in driver.page_source:
                    print('Robot')
                    return ('Robot','Robot')
                if 'images-na.ssl-images-amazon.com' not in driver.page_source:
                    print('Loading')
                    return ('Loading','Loading')
                break

            except TimeoutException:
                print('Timeout')
                return ('Timeout','Timeout')
            except Exception as e:
                print('Connection Refused')
                return ('Connection','Connection')
        driver_source = driver.page_source
        soup_pro = self.getSoup(driver_source)
        soup = self.get_post_soup(soup_pro)
        try:
            items_div = soup.select("ul.s-result-list li[id*=result] div.s-item-container")
            print(items_div[0])
        except:
            try:
                items_div = soup.select("div.s-result-item")
            except:
                items_div = None
                pass
        lst = []
        if items_div == None:
            return (lst,driver_source)
        else:
            for item in items_div:
                try:
                    # pro_check = "AZ" + item.parent["data-asin"]
                    image_div = item.select_one("img.s-access-image")
                    pro_check = image_div["alt"]
                except:
                    try:
                        # pro_check = "AZ" + item["data-asin"]
                        pro_check = item.select_one("div.s-image-square-aspect img")["alt"]
                    except:
                        try:
                            pro_check = item.select_one("div.s-image-fixed-height img")["alt"]
                        except:
                            try:
                                pro_check = item.select_one("h5.s-line-clamp-2 span").text.strip()
                            except:
                                pro_check = item.find("h2", {'class':'s-access-title'}).text.strip()

                try:
                    brandtitle = item.find("div",{'class': 'a-row a-spacing-small a-grid-vertical-align a-grid-center'}).find("img")['alt']
                    pro_check1 = brandtitle + ' ' + pro_check
                except:
                    try:
                        brandtitle = item.find("div",{'class': 'a-row a-spacing-small a-grid-vertical-align a-grid-center'}).find("span").text.strip()
                        pro_check1 = brandtitle + ' ' + pro_check
                    except:
                        pro_check1 = 'ojieojfowemfoweefijwe0'

                try:
                    link_div = item.select_one("a.s-access-detail-page")
                    pro_url = self.getAbsUrl(url_link, link_div["href"])
                except:
                    linkkk = item.select_one("span.rush-component a.a-link-normal")["href"]
                    pro_url = self.getAbsUrl(url_link, linkkk)
                lst.append({'url': pro_url, 'Title': pro_check, 'Title1': pro_check1})
            return (lst,soup)

    def scrape_data(self,data):
        is_next = True
        proxy, driver,display = self.getProxyWorking()
        url_link = data['url']
        cat = data['cat']
        subcat = data['subcat']
        dic_data = {
            'url': url_link,
            'driver': driver,
        }
        while is_next:
            check_data = True
            while check_data:
                try:
                    items_div,soup = self.getMainPage(dic_data)
                    if items_div == 'Robot' or items_div == 'Timeout' or items_div == 'Loading' or items_div == 'Connection':

                        # proo = AmazonProxies.objects.get(proxy=proxy)
                        # proo.delete()
                        driver.quit()
                        display.stop()
                        if items_div == 'Robot':
                            sleep(300)
                        # display.stop()
                        proxy, driver,display = self.getProxyWorking()
                        dic_data['driver'] = driver
                        continue
                    check_data = False
                except Exception as e:
                    print(e)
                    # proo = AmazonProxies.objects.get(proxy=proxy)
                    # proo.count -= 1
                    # proo.save()
                    # proxy,driver, display = self.getProxyWorking()
                    # dic_data['driver'] = driver
            for current_item_div in items_div:
                try:
                    if AllProducts.objects.filter(SNR_Title=current_item_div['Title'],SNR_Available='Amazon').exists() == False and AllProducts.objects.filter(SNR_Title=current_item_div['Title1'],SNR_Available='Amazon').exists() == False:
                        dic = {
                            'url': current_item_div['url'],
                            'driver': driver,
                            'cat': cat,
                            'subcat': subcat
                        }
                        check = True
                        while check:
                            try:
                                res = self.individulaProduct(dic)
                                if res == 'Robot' or res == 'Timeout' or res == 'Loading' or res == 'Connection':
                                    # proo = AmazonProxies.objects.get(proxy=proxy)
                                    # proo.delete()
                                    driver.quit()
                                    display.stop()
                                    if items_div == 'Robot':
                                        sleep(300)
                                    # display.stop()
                                    proxy, driver,display = self.getProxyWorking()
                                    dic['driver'] = driver
                                    continue
                                check = False
                            except Exception as e:
                                print(e)
                                # proo = AmazonProxies.objects.get(proxy=proxy)
                                # proo.count -= 1
                                # proo.save()
                                # try:
                                #     res = self.individulaProduct(dic)
                                #     if res == 'Robot':
                                #         continue
                                #     check = False
                                # except:
                                #     pass

                except NoSuchElementException as e:
                    print(e)

                except ElementNotVisibleException as r:
                    print(r)

                except Exception as e:
                    print(e)
                    pass

            try:
                next_div = soup.select_one("a#pagnNextLink")["href"]
            except:
                try:
                    next_div = soup.select_one("li.a-last a")["href"]
                except:
                    # driver.quit()
                    # display.stop()
                    next_div = False
                    is_next = False

            if next_div:
                url = self.getAbsUrl(url_link, next_div)
                dic_data['url'] = url
                is_next = True

    def get_post_soup(self,soup):
        temp = soup.select_one("div#rightResultsATF")
        if not temp:
            temp = soup.select_one("div[id*=search-results]")
        if not temp:
            temp = soup.select_one("div.s-right-column")

        return temp

def runThreads(file):
    index = file['index']
    if index == 1:
        blue = Products()
        blue.get_data_Textfile()
    if index == 2:
        sleep(60)
        red = Products()
        red.get_data_Textfile()
    if index == 3:
        sleep(120)
        green = Products()
        green.get_data_Textfile()
    if index == 4:
        yellow = Products()
        yellow.get_data_Textfile()
    if index == 5:
        pink = Products()
        pink.get_data_Textfile()

def main():
    file = [{'index':1},{'index':2},{'index':3}]

    p = ThreadPool(3)
    result = p.map(runThreads,file)
    p.close()
    p.join()

    # title = 'SMILING PINKER Girls Cardigan Sweater School Uniforms Button Long Sleeve Knit Tops'
    #
    # proo = AllProducts.objects.filter(SNR_Title=title,SNR_Available='Amazon')
    # print(proo

    # blue = Products()
    # blue.get_data_Textfile()

    # blu = Products()
    # proxy,driver,display = blu.getProxyWorking()
    # dic = {'url':'https://www.amazon.com/s/ref=lp_2975276011_nr_n_1?fst=as%3Aoff&rh=n%3A2619533011%2Cn%3A%212619534011%2Cn%3A2975241011%2Cn%3A2975276011%2Cn%3A2975278011&bbn=2975276011&ie=UTF8&qid=1552911198&rnid=2975276011','driver':driver,'cat':'ff','subcat':'dd'}
    # print(blu.getMainPage(dic)

    # blu = Products()
    # proxy, driver, display = blu.getProxyWorking()
    # dic = {'url': 'https://www.amazon.com/gp/bestsellers/industrial/3094000011/ref=sr_bs_3_3094000011_1',
    #        'driver': driver, 'cat': 'tt', 'subcat': 'ytr'}
    # blu.individulaProduct(dic)



if __name__ == '__main__':
    main()

