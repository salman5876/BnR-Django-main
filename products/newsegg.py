import requests
from bs4 import BeautifulSoup
import time
from .serializers import TV_Serializer,Applinces_Serializer,Cams_Serializer,Office_Serializer,VideoGames_Serializer,Health_Serializer


class newEggAPI():
    def newEggHealth(self, request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=665&N=100199234&IsNodeId=1'
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
            serializer = Health_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 60):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100199234&IsNodeId=1&bop=And&Page=' + str(
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
                serializer = Health_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1



    def newEggTV(self, request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=31&N=100198692%2050008957%2050010405%2050011043%2050011059%2050087708%2050091965&IsNodeId=1'
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
            serializer = TV_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 5):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100198692%2050008957%2050010405%2050011043%2050011059%2050087708%2050091965&IsNodeId=1&bop=And&Page=' + str(
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
                serializer = TV_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1

    def newEggAppliances(self,request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=312&N=100199428%2050008025%2050010163%2050010691%2050012785%2050075172%2050081237&IsNodeId=1'
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
            serializer = Applinces_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 5):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100199428%2050008025%2050010163%2050010691%2050012785%2050075172%2050081237&IsNodeId=1&bop=And&Page=' + str(
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
                serializer = Applinces_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1




    def newEggCams(self,request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100202254%2050001213%2050001247%2050042609%2050087529%2050147182'
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
            serializer = Cams_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 3):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100202254%2050001213%2050001247%2050042609%2050087529%2050147182&IsNodeId=1&bop=And&Page=' + str(
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
                serializer = Cams_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1






    def newEggOffice(self,request):
        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&Category=125&N=100201438%2050001009%2050001467%2050081237%2050093636%2050097055%2050129358&IsNodeId=1'
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
            serializer = Office_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 5):
            time.sleep(count + 40)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100201438%2050001009%2050001467%2050081237%2050093636%2050097055%2050129358&IsNodeId=1&bop=And&Page=' + str(
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
                serializer = Office_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1





    def newEgggGames(self,request):


        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100202391&IsNodeId=1&name=PC%20Games&isdeptsrh=1'
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
            serializer = VideoGames_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        count = 2
        while (count < 5):
            time.sleep(count + 4)
            url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100202391&IsNodeId=1&bop=And&Page=' + str(
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
                serializer = VideoGames_Serializer(data=request)
                # print("bestbuy calling")
                print(serializer)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print("bad json")
            count += 1


        url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100202381&IsNodeId=1&name=PS4%20Video%20Games&isdeptsrh=1'
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
            serializer = VideoGames_Serializer(data=request)
            # print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                print("bad json")

        #
        #
        # url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&IsNodeId=1&N=100202378%2050001541%2050001781%2050002003'
        # source = requests.get(url)
        # plain_text = source.text
        # # print plain_text
        #
        #
        #
        #
        # soup = BeautifulSoup(plain_text, "lxml")
        # for link in soup.findAll('div', {'class': 'item-container'}):
        #     request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
        #     request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
        #     # for li in link.findAll('img'):
        #     #     print "https:"+li.get("src") #warranty and image
        #
        #     x = link.find('a', {'class': 'item-img'})  # product image
        #     request["SNR_ImageURL"]= "https:" + x.find('img').get("src")
        #     try:
        #         x = link.find('a', {'class': 'item-brand'})  # product url
        #         request["SNR_Brand"] = "https:" + x.find('img').get("src")
        #     except:
        #         request["SNR_Brand"] = "No Brand"
        #
        #     try:
        #         x = link.find('li', {'class': 'price-current'})
        #         request["SNR_Price"] = x.find('strong').text
        #     except:
        #         request["SNR_Price"] = "00"
        #
        #     try:
        #         x = link.find('ul', {'class': 'item-features'})
        #         for feature in x.findAll('li'):
        #             if ("Model #" in feature.text):
        #                 request["SNR_ModelNo"] = feature.text
        #             if ("Item #" in feature.text):
        #                 request["SNR_SKU"] =  feature.text
        #     except:
        #         request["SNR_SKU"] ="00"
        #         request["SNR_ModelNo"] ="00"
        #
        #     request["SNR_Available"] = "Newegg"
        #     request["SNR_Description"] = "Visit site to see description"
        #     request["SNR_UPC"] ="00"
        #     serializer = VideoGames_Serializer(data=request)
        #     # print("bestbuy calling")
        #     print(serializer)
        #     if serializer.is_valid():
        #         serializer.save()
        #     else:
        #         print("bad json")
        #
        # count = 2
        # while (count < 2):
        #     time.sleep(count + 4)
        #     url = 'https://www.newegg.com/global/au/Product/ProductList.aspx?Submit=ENE&N=100201438%2050001009%2050001467%2050081237%2050093636%2050097055%2050129358&IsNodeId=1&bop=And&Page=' + str(
        #         count) + '&pagesize=36&order=bestmatch'
        #     source = requests.get(url)
        #     plain_text = source.text
        #     # print plain_text
        #     soup = BeautifulSoup(plain_text, "lxml")
        #     for link in soup.findAll('div', {'class': 'item-container'}):
        #         request["SNR_Title"] = link.find('a', {'class': 'item-title'}).text  # title
        #         request["SNR_ProductURL"] = link.find('a', {'class': 'item-title'}).get('href')  # product url
        #         # for li in link.findAll('img'):
        #         #     print "https:"+li.get("src") #warranty and image
        #
        #         x = link.find('a', {'class': 'item-img'})  # product image
        #         request["SNR_ImageURL"] = "https:" + x.find('img').get("src")
        #         try:
        #             x = link.find('a', {'class': 'item-brand'})  # product url
        #             request["SNR_Brand"] = "https:" + x.find('img').get("src")
        #         except:
        #             request["SNR_Brand"] = "No Brand"
        #
        #         try:
        #             x = link.find('li', {'class': 'price-current'})
        #             request["SNR_Price"] = x.find('strong').text
        #         except:
        #             request["SNR_Price"] = "00"
        #
        #         try:
        #             x = link.find('ul', {'class': 'item-features'})
        #             for feature in x.findAll('li'):
        #                 if ("Model #" in feature.text):
        #                     request["SNR_ModelNo"] = feature.text
        #                 if ("Item #" in feature.text):
        #                     request["SNR_SKU"] = feature.text
        #         except:
        #             request["SNR_SKU"] = "00"
        #             request["SNR_ModelNo"] = "00"
        #
        #         request["SNR_Available"] = "Newegg"
        #         request["SNR_Description"] = "Visit site to see description"
        #         request["SNR_UPC"] = "00"
        #         serializer = VideoGames_Serializer(data=request)
        #         # print("bestbuy calling")
        #         print(serializer)
        #         if serializer.is_valid():
        #             serializer.save()
        #         else:
        #             print("bad json")
        #     count += 1
        #
        #
