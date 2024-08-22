import re
from scrapetools import *
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer, DailyDeals_Serializer,AmazonURLs_Serializer
from products.models import AmazonURLs, AllProducts, AmazonProxies
# proxy = getProxyWorking()
# proxy = proxy['http']

url_data = 'https://www.amazon.com/Story-Behind-Cinco-Holiday-Histories/dp/1725300389/ref=sr_1_250?qid=1555384630&s=books&sr=1-250'
# url_data = 'https://www.amazon.com/Maya-Scientific-Ancient-American-People/dp/1562945971/ref=sr_1_377?qid=1555384739&s=books&sr=1-377'
# url_data = 'https://www.amazon.com/Aquaman-Jason-Momoa/dp/B07PPK1BXZ/ref=lp_2650363011_1_3?s=movies-tv&ie=UTF8&qid=1554882484&sr=1-3'
url_data1 = 'https://www.amazon.com/gp/product/B07BMHPM2H/ref=s9_acsd_zgift_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-12&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_r=75JQZJKSZ85YF5T0R26S&pf_rd_t=101&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_p=96fc1f4c-c93e-5f1f-aebd-7ea5c1a8b7cd&pf_rd_i=2476517011'
url_data2 = 'https://www.amazon.com/Amazon-Essentials-Regular-Fit-Long-Sleeve-Flannel/dp/B073XQBL8X/ref=lp_1045630_1_2?s=apparel&ie=UTF8&qid=1545117982&sr=1-2&nodeID=1045630&psd=1&th=1'
url_data3 = 'https://www.amazon.com/gp/product/B079NBMTWY/ref=s9_acss_bw_cg_TVChoic1_2a1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=MBE1C2DWDHZ9N5P7GTX0&pf_rd_t=101&pf_rd_p=3896f6e0-793c-42be-8970-4d0b11819fb5&pf_rd_i=1266092011'
url_data4 = 'https://www.amazon.com/Native-Jefferson-Regatta-Medium-Little/dp/B074HBLYVN/ref=lp_3420561011_1_1/146-7784815-6172701?s=apparel&ie=UTF8&qid=1545308002&sr=1-1&nodeID=3420561011&psd=1'
url_data5 = 'https://www.amazon.com/Bigib-Non-Slip-Barefoot-Aqua-Socks-Boys-Girls-Toddler/dp/B07DGFH2SB/ref=lp_3420561011_1_4/145-1883620-9419768?s=apparel&ie=UTF8&qid=1545471694&sr=1-4&nodeID=3420561011&psd=1'
url_data6 = 'https://www.amazon.com/APRLL-Women-Sleeve-Turtleneck-Blouse/dp/B07DFFY37K/ref=lp_2368343011_1_27/141-9544998-8613149?s=apparel&ie=UTF8&qid=1545650173&sr=1-27&nodeID=2368343011&psd=1'
url_data7 = 'https://www.amazon.com/Just-Love-Henley-Pants-6732-10195-M/dp/B07DF5TBG3/ref=lp_2368343011_1_12/132-9245822-0605643?s=apparel&ie=UTF8&qid=1545653035&sr=1-12&nodeID=2368343011&psd=1'
url_data8 = 'https://www.amazon.com/Red-Kap-Womens-Pleated-Slacks/dp/B00DUDO2QC/ref=sr_1_57/130-8517998-5298261?s=apparel&ie=UTF8&qid=1547473334&sr=1-57&nodeID=2528697011&psd=1'
url_data9 = 'https://www.amazon.com/Red-Food-Cart/dp/B07KVV95ZY/ref=lp_6685279011_1_2?s=art&ie=UTF8&qid=1553256586&sr=1-2'

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % proxy)

# driver = webdriver.Chrome(executable_path="../chromedriver",chrome_options = chrome_options)
# driver1 = webdriver.Chrome(executable_path="../chromedriver",chrome_options = chrome_options)
# driver2 = webdriver.Chrome(executable_path="../chromedriver",chrome_options = chrome_options)
# objesc = AllProducts.objects.filter(SNR_Category='Women')[:10000]
# objesc = AllProducts.objects.filter(SNR_Category='Men')[:10000]
# objesc = AllProducts.objects.filter(SNR_Category='Girl')[:10000]


def scrapppp(index):
    driver = webdriver.Chrome(executable_path="../chromedriver", chrome_options=chrome_options)
    object = AllProducts.objects.filter(SNR_Category='Women')[:10000]
    while True:
        for url in object.iterator():
            driver.get(url.SNR_ProductURL)
            if 'automated access' in driver.page_source:
                print 'Robot'
                sleep(1000000)
p = ThreadPool(3)
lst = list(range(3))
result = p.map(scrapppp,lst)
p.close()
p.join()
request = {}
try:

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
    request["SNR_ProductURL"] = url_data
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


except NoSuchElementException as e:
    print e

except ElementNotVisibleException as r:
    print r

except Exception as e:
    print e
    pass
