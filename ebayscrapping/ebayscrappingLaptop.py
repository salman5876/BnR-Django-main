

import string
import requests
import json
import unicodedata
from bs4 import BeautifulSoup
class EbayScrapping():
    def Scrapper(self, request):
        page = 1;
        count=1;

        # urls=['https://www.ebay.com/sch/Cell-Phones-Smartphones/9355/i.html?LH_BIN=1&_pgn=1&_skc=50','https://www.ebay.com/sch/Display-Phones/136699/i.html?LH_BIN=1&_pgn=1&_skc=50','https://www.ebay.com/sch/Vintage-Cell-Phones/182073/i.html?LH_BIN=1&_pgn=1&_skc=50','https://www.ebay.com/sch/Phone-Cards-SIM-Cards/146492/i.html?LH_BIN=1&_pgn=1&_skc=50']
        urls=['https://www.ebay.com/rpp/electronics-en-computers']
        pagesurl=[]

        for url in urls:
            page = 1;
            url=string.replace(url,'pgn=1','pgn='+str(page))
            print 'url............'+url
            source = requests.get(url)
            plain_text = source.text
            page=page+1;

            soup = BeautifulSoup(plain_text, "lxml")

            for link in soup.findAll('ul', {'class': 'navigation-list nested'}):
                print 'count..'+str(count)
                count=count+1;
                # try:


                linkprod=link.find('a').get('href')
                linkprod=linkprod.replace('html','html?LH_BIN=1&_pgn=1&_skc=50')

                pagesurl.append(linkprod)

        for url in pagesurl:
            page = 1;
            while page < 150:
                url = string.replace(url, 'pgn='+str(page), 'pgn=' + str(page))
                print 'url............' + url
                source = requests.get(url)
                plain_text = source.text
                page = page + 1;

                soup = BeautifulSoup(plain_text, "lxml")
                # print plain_text

                for link in soup.findAll('li', {'class': 'sresult lvresult clearfix li shic'}):
                    print 'count..' + str(count)
                    count = count + 1;
                    # try:

                    try:

                        print 'link....' + link.find('a', {'class': 'img imgWr2'}).get('href')
                        linkprod = link.find('a', {'class': 'img imgWr2'}).get('href')
                    except:
                        print 'link....' + link.find('a', {'class': 'img imgWr2 null'}).get('href')
                        linkprod = link.find('a', {'class': 'img imgWr2 null'}).get('href')

                    print 'IMAGE....' + link.find('img', {'class': 'img'}).get('src')
                    print 'Title....' + link.find('a', {'class': 'vip'}).text
                    price = link.find('span', {'class': 'bold'}).text.strip().replace(",", "")
                    print (price[1:])
                    print 'Subtitle....' + link.find('div', {'class': 'lvsubtitle'}).text
                    print 'SKU....' + link.get('id')
                    # try:

                    request["SNR_Price"] = (price[1:])

                    request["SNR_Brand"] = "No Brand"
                    request["SNR_Available"] = "Ebay"
                    try:
                        request["SNR_Description"] = "Visit site to see description"
                    except:
                        request["SNR_Description"] = link.find('div', {'class': 'lvsubtitle'}).text

                    request["SNR_Title"] = link.find('a', {'class': 'vip'}).text
                    request["SNR_ProductURL"] = linkprod
                    request["SNR_ImageURL"] = link.find('img', {'class': 'img'}).get('src')
                    request["SNR_ModelNo"] = "00"
                    request["SNR_UPC"] = "00"
                    request["SNR_Category"] = "Cell Phones"
                    request["SNR_SKU"] = link.get('id')
                    request["SNR_isShow"] = False

                    serializer1 = AllProducts_Serializer(data=request)
                    try:
                        print(serializer1)
                        if serializer1.is_valid():
                            print("---")
                            serializer1.save()
                        else:
                            print('serlizor not valid')
                    except:
                        print serializer1.errors
                        # except:
                        #     continue

                for link in soup.findAll('li', {'class': 'sresult lvresult clearfix li'}):
                    print 'count..' + str(count)
                    count = count + 1;
                    # try:

                    try:

                        print 'link....' + link.find('a', {'class': 'img imgWr2'}).get('href')
                        linkprod = link.find('a', {'class': 'img imgWr2'}).get('href')
                    except:
                        print 'link....' + link.find('a', {'class': 'img imgWr2 null'}).get('href')
                        linkprod = link.find('a', {'class': 'img imgWr2 null'}).get('href')

                    print 'IMAGE....' + link.find('img', {'class': 'img'}).get('src')
                    print 'Title....' + link.find('a', {'class': 'vip'}).text
                    price = link.find('span', {'class': 'bold'}).text.strip().replace(",", "")
                    print (price[1:])
                    print 'Subtitle....' + link.find('div', {'class': 'lvsubtitle'}).text
                    print 'SKU....' + link.get('id')
                    # try:

                    request["SNR_Price"] = (price[1:])

                    request["SNR_Brand"] = "No Brand"
                    request["SNR_Available"] = "Ebay"
                    try:
                        request["SNR_Description"] = "Visit site to see description"
                    except:
                        request["SNR_Description"] = link.find('div', {'class': 'lvsubtitle'}).text

                    request["SNR_Title"] = link.find('a', {'class': 'vip'}).text
                    request["SNR_ProductURL"] = linkprod
                    request["SNR_ImageURL"] = link.find('img', {'class': 'img'}).get('src')
                    request["SNR_ModelNo"] = "00"
                    request["SNR_UPC"] = "00"
                    request["SNR_Category"] = "Cell Phones"
                    request["SNR_SKU"] = link.get('id')
                    request["SNR_isShow"] = False

                    serializer1 = AllProducts_Serializer(data=request)
                    try:
                        print(serializer1)
                        if serializer1.is_valid():
                            print("---")
                            serializer1.save()
                        else:
                            print('serlizor not valid')
                    except:
                        print serializer1.errors
                        # except:
                        #     continue

        print pagesurl


EbayScrapping().Scrapper({})