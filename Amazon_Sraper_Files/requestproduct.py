import re
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains

# proxy = getProxyWorking()
# proxy = proxy['http']

url_data = 'https://www.amazon.com/KingSize-Lightweight-Cotton-Muscle-Big-4Xl/dp/B005GQAKEE/ref=lp_2476518011_1_1/134-0197383-7546749?s=apparel&ie=UTF8&qid=1549109461&sr=1-1&nodeID=2476518011&psd=1'
url_data1 = 'https://www.amazon.com/QPNGRP-Sleeve-Hooded-T-Shirt-WineRed/dp/B07MYT9HBS/ref=lp_1258644011_1_1/134-7576621-9770859?s=apparel&ie=UTF8&qid=1549109461&sr=1-1&nodeID=1258644011&psd=1'
url_data2 = 'https://www.amazon.com/Mountain-Hardwear-Butterman-Crew-Pullover/dp/B078J2RP7J/ref=lp_2211975011_1_1/145-7788738-7789748?s=apparel&ie=UTF8&qid=1549109461&sr=1-1&nodeID=2211975011&psd=1'
url_data3 = 'https://www.amazon.com/Skechers-Advantage-Mcallen-Black-Charcoal/dp/B07K4D4MY3/ref=lp_6796861011_1_1/139-8801747-1921504?s=apparel&ie=UTF8&qid=1549109462&sr=1-1&nodeID=6796861011&psd=1'
url_data4 = 'https://www.amazon.com/Mens-Piece-Button-Blazer-Trousers/dp/B07KWNBG5J/ref=lp_1045686_1_1/130-9355754-8368214?s=apparel&ie=UTF8&qid=1549109461&sr=1-1&nodeID=1045686&psd=1'
url_data5 = 'https://www.amazon.com/Bigib-Non-Slip-Barefoot-Aqua-Socks-Boys-Girls-Toddler/dp/B07DGFH2SB/ref=lp_3420561011_1_4/145-1883620-9419768?s=apparel&ie=UTF8&qid=1545471694&sr=1-4&nodeID=3420561011&psd=1'
url_data6 = 'https://www.amazon.com/APRLL-Women-Sleeve-Turtleneck-Blouse/dp/B07DFFY37K/ref=lp_2368343011_1_27/141-9544998-8613149?s=apparel&ie=UTF8&qid=1545650173&sr=1-27&nodeID=2368343011&psd=1'
url_data7 = 'https://www.amazon.com/Just-Love-Henley-Pants-6732-10195-M/dp/B07DF5TBG3/ref=lp_2368343011_1_12/132-9245822-0605643?s=apparel&ie=UTF8&qid=1545653035&sr=1-12&nodeID=2368343011&psd=1'
url_data8 = 'https://www.amazon.com/Red-Kap-Womens-Pleated-Slacks/dp/B00DUDO2QC/ref=sr_1_57/130-8517998-5298261?s=apparel&ie=UTF8&qid=1547473334&sr=1-57&nodeID=2528697011&psd=1'
url_data9 = 'https://www.amazon.com/Global-Heavyweight-Sherpa-Hoodie-Sweatshirt/dp/B01MSWM33G/ref=lp_1258644011_1_17/130-4450310-4763848?s=apparel&ie=UTF8&qid=1549020581&sr=1-17&nodeID=1258644011&psd=1'
url_data10 = 'https://www.amazon.com/Quanii-Sweatshirt-Pullover-Hoodies-Sweater/dp/B07L68VWJQ/ref=lp_1258644011_1_6/140-3753899-7845856?s=apparel&ie=UTF8&qid=1549258827&sr=1-6&nodeID=1258644011&psd=1'
url_data11 = 'https://www.amazon.com/Wizard-Glasses-Unisex-Sweatshirt-Fashion/dp/B01N117MGT/ref=sr_1_124?s=apparel&ie=UTF8&qid=1549462080&sr=1-124&nodeID=1258644011&psd=1'


print ','.join(('AAAAA','BBBBB','CCCCCC')).encode('utf-8').strip()


rawdata = requests.get(url_data11)
request = {}
try:
    soup_pro = BeautifulSoup(rawdata.text, "lxml")
    pattern = re.compile(r'ImageBlockATF', re.MULTILINE | re.DOTALL)
    img = soup_pro.find("script", text=pattern)
    ImageText = []
    try:
        imgtext = re.search(r'initial(.*?)colorToAsin', img.string.strip(), flags=re.DOTALL | re.MULTILINE).group(1).strip()[3:-20]
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
        imgtext = re.search(r'imageGalleryData(.*?)centerColMargin', img.string.strip(),flags=re.DOTALL | re.MULTILINE).group(1).strip()[3:-11]
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
        brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a")['href'].split('/b', 1)[0].strip('/')
    except:
        try:
            brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").text.strip()
        except:
            brand = soup_pro.find("div",{"id":"merchant-info"}).find("a").text.strip()
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
    request["SNR_ProductURL"] = url_data9
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
                Price = soup_pro.find('span', {'class': 'a-size-base a-color-price a-color-price'}).text.strip().split('$', 1)[1]
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

    print request

except NoSuchElementException as e:
    print e

except ElementNotVisibleException as r:
    print r

except Exception as e:
    print e
    pass
