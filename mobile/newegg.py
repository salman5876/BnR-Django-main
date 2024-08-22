import requests
from bs4 import BeautifulSoup
import time
from .serializer import Mobile_Serializer


class newEggAPI():
    def newEggMobiles(self,request):
        url = 'https://www.newegg.com/product/productlist.aspx?submit=ene&n=100167543 600025861 600025862 600025874 600025878 600025881 600551125 600025860 600025864 600025866 600025876 600025877 600025880 600025883 600025889 600025890 600077252 600078906 600095334 600476000 600482513 600484844 600547686 600551649 600415427&isnodeid=1&bop=and&pagesize=36&order=bestmatch'
        source = requests.get(url)
        plain_text = source.text
        # print plain_text




        soup = BeautifulSoup(plain_text, "lxml")
        for link in soup.findAll('div', {'class': 'item-container'}):
            request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
            request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
            # for li in link.findAll('img'):
            #     print "https:"+li.get("src") #warranty and image

            x = link.find('a', {'class': 'item-img'})  # product image
            request["SNR_ImageURL"]= "https:" + x.find('img').get("src")
            try:
                x = link.find('a', {'class': 'item-brand'})  # product url
                request["SNR_Brand"] = "https:" + x.find('img').get("src")
            except:
                request["SNR_Brand"] = "No Brand"

            try:
                x = link.find('li', {'class': 'price-current'})
                request["SNR_Price"] = x.find('strong').text
            except:
                request["SNR_Price"] = "00"

            try:
                x = link.find('ul', {'class': 'item-features'})
                for feature in x.findAll('li'):
                    if ("Model #" in feature.text):
                        request["SNR_ModelNo"] = feature.text
                    if ("Item #" in feature.text):
                        request["SNR_SKU"] =  feature.text
            except:
                request["SNR_SKU"] ="00"
                request["SNR_ModelNo"] ="00"

            request["SNR_Available"] = "Newegg"
            request["SNR_Description"] = "Visit site to see description"
            request["SNR_UPC"] ="00"
            serializer = Mobile_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 60):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/product/productlist.aspx?submit=ene&n=100167543 600025861 600025862 600025874 600025878 600025881 600551125 600025860 600025864 600025866 600025876 600025877 600025880 600025883 600025889 600025890 600077252 600078906 600095334 600476000 600482513 600484844 600547686 600551649 600415427&isnodeid=1&bop=and&Page=' + str(
                count) + '&pagesize=36&order=bestmatch'
            source = requests.get(url)
            plain_text = source.text
            # print plain_text
            soup = BeautifulSoup(plain_text, "lxml")
            for link in soup.findAll('div', {'class': 'item-container'}):
                request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
                request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
                # for li in link.findAll('img'):
                #     print "https:"+li.get("src") #warranty and image

                x = link.find('a', {'class': 'item-img'})  # product image
                request["SNR_ImageURL"] = "https:" + x.find('img').get("src")
                try:
                    x = link.find('a', {'class': 'item-brand'})  # product url
                    request["SNR_Brand"] = "https:" + x.find('img').get("src")
                except:
                    request["SNR_Brand"] = "No Brand"

                try:
                    x = link.find('li', {'class': 'price-current'})
                    request["SNR_Price"] = x.find('strong').text
                except:
                    request["SNR_Price"] = "00"

                try:
                    x = link.find('ul', {'class': 'item-features'})
                    for feature in x.findAll('li'):
                        if ("Model #" in feature.text):
                            request["SNR_ModelNo"] = feature.text
                        if ("Item #" in feature.text):
                            request["SNR_SKU"] = feature.text
                except:
                    request["SNR_SKU"] = "00"
                    request["SNR_ModelNo"] = "00"

                request["SNR_Available"] = "Newegg"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_UPC"] = "00"
                serializer = Mobile_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1
