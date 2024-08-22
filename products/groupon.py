from .serializers import TV_Serializer, Cams_Serializer, CarsElec_Serializer, VideoGames_Serializer, Toys_Serializer, \
    Smarthomes_Serializer, Audio_Serializer, Software_Serializer, Applinces_Serializer, Movies_Serializer, \
    Office_Serializer
import requests
import json
import unicodedata
from rest_framework.response import Response  # to send specific response
from rest_framework import status
from bs4 import BeautifulSoup

baseAddress = "http://localhost:8000/"
img=""

class GroupOnAPI():


    def groupCams(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/camera-video-and-surveillance?brand=3350ca50-e4d5-477f-a623-1a7ef4f56fce%2C34ed70c5-e9d0-412f-9014-c8ccbf5dc27f%2C98210654-11e3-44ea-90c3-b73defd7237c%2C9a48803a-f596-4146-b405-921a5282e1d4&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    request["SNR_ImageURL"] = "https:"+img
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Cams_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1





    def groupCarsElectronics(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/car-electronics-and-gps?brand=085b8ef1-6195-4936-9a78-0ab6409a4af2%2C0cad1ce7-60fe-453f-9640-cc29f4cfdd0b%2C119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C3061f93c-4a05-4c3a-8bab-65618ecd042b%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C434bb387-8e82-446f-9d25-c0578ab24600%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C50e5275a-2712-4653-91f8-410197177d7a%2C5a443675-0b42-441e-8d60-378f8fd6ba62%2C5f6e1462-a7df-4dd5-9a62-ee1077b7ffb8%2C5fca46bd-c4e3-4eb3-a329-333cca916127%2C904231b9-f837-4dab-8f5f-ad3dc9acd3ad%2C965b4979-61eb-4150-a63e-6a55b150c70c%2C990dc215-e0fe-4b04-97e6-81d10e80de31%2Ca093638f-2739-42d2-a6d2-7f5777cda678%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Cc756c723-9cbf-4d2c-bb4c-3a7d53fa3357%2Cdb89a50c-3579-4a71-91a7-c2c4daa93ecb%2Cdb92452b-396b-4e7a-932d-ee6bdcea71d9%2Cf457b68e-928e-453e-8ced-641c244dbf6d&page=' + str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    request["SNR_ImageURL"] ="https:"+ img
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = CarsElec_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1



    def groupOffice(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/office-and-school-supplies?brand=1cdf8c46-f6d5-43aa-a048-2a88f15f5f35%2C1f07e9cf-f406-4b9c-98b7-f1cfa8a695d5%2C23d34b72-ea5b-464e-b1c9-092611f27b78%2C2489602b-5757-4165-bca3-11d34167f053%2C2a5b42cd-3c7a-4799-a1a1-77bca921865e%2C3350ca50-e4d5-477f-a623-1a7ef4f56fce%2C3ffae6d6-2994-43e8-ae31-d564124ebb4a%2C41f7972b-117b-46e3-8b02-17aa2d2873f9%2C47ab2b5c-dfbd-45cf-b051-bbeb0ae5c553%2C4bf4d230-1f7e-426e-a095-e126c1469a28%2C51198fdc-779e-4881-bc41-129ef8f11600%2C7c2226ea-8563-4e5e-bbc3-6e8b4a3e2b6c%2C8efa5611-0f81-4233-93f1-e922c8f6dc73%2Ca7ad779a-8137-4e93-8592-ea6dd9ef6088%2Cb1ccee99-5a63-4dfc-81cf-6044bdabbd19%2Cec3dbb6d-8c0f-4904-b213-527843f3dc49&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                img=""

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        try:
                            img = li.get('data-high-quality')
                            # print img
                        except:
                            img="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] = price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Office_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1






    def groupAudio(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/portable-audio?brand=02a23818-b476-437a-816e-3565ae5c8418%2C0b99c673-3670-4711-b3a4-fa4632af81b4%2C119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C11faef5a-923c-4dd2-bfc3-36c4dff8d973%2C1f27b9c3-dfb0-46c7-8c80-a6c38b8a4dfe%2C20c800dc-e500-460e-9c3d-0c64f6e452be%2C3e4af2af-b7cf-48d2-bf19-e5e6b2a89076%2C3f00dac3-a514-4a7f-846e-2cccae6cebf9%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C5fca46bd-c4e3-4eb3-a329-333cca916127%2C70fde650-5c08-49df-b014-9121a4379144%2C90b24dac-81b8-4f82-a006-5e66ff7f70a8%2C92d4f60c-f3a7-4d1d-8b9c-3f1fe679f5e5%2C9ca6fd1c-77ea-4782-be35-226dea85eb01%2C9e0b0f53-c249-4445-9a98-bf72f2e2f2de%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Ca5b9ec70-1f8f-48bc-a250-08cb3bb00d45%2Caccabc93-7ef8-4af8-8a74-ce5f57eb798e%2Caf90baa3-69d5-43cb-b534-64ea28b17723%2Cb0d88b2c-41b9-40f9-a5ea-3f62573b90f7%2Cd1fefd92-013c-46a4-a2ef-5c4362ff72cd%2Cd83f37a0-194e-494c-ac2d-c1b6936ee369%2Cdb89a50c-3579-4a71-91a7-c2c4daa93ecb%2Ce2855e0b-a6aa-4f9b-9c66-9db69f8e1e97%2Ce73aec2d-a484-4d8d-bf1a-842b694e3feb&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Audio_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1




    def groupSoftware(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/software?brand=067e0705-93cf-4e3c-a1e9-7081412d3b92%2C087187e0-f6c5-47a1-9b94-a9abecb9eaf6%2C1933fbbb-5d78-4fdd-ad12-3339d67c7a0c%2C1fed83a9-e10d-45a7-92e0-41da73cc76d5%2C4215afd8-96bc-4234-a1c5-933a7989c52a%2C4802dc99-68ff-4574-8105-5dd1fe3614c8%2C51198fdc-779e-4881-bc41-129ef8f11600%2C5d54d3c1-5be0-4578-8a31-80334892afd3%2C834f870f-bd4b-4a2a-8c13-ddfcb9b66a84%2C91fd0374-e935-49ff-8fbe-8b2e203c1730%2Cab74da87-00f5-497c-bdc0-df8c2514aa26%2Ccb0d6714-829e-476e-96bd-5e7227ad8fc7%2Cdbe120bb-4114-4799-8a2f-fea629c4c009%2Ce4529dec-38c1-4915-b0f1-713f3f9448d5&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img = ""
                    for li in link.findAll('img', {'class': 'cui-image'}):

                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None or img!="":

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Software_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1



    def groupGames(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/v2-gaming?brand=01be065e-454b-46b8-8373-7e97c4cc4e16%2C0afe0489-2d18-40b7-8a8d-f93987b0b9b2%2C143c38ff-78ac-4075-97a7-0ce9489504ce%2C175e8abd-d8cd-44fd-90d0-b0cc38aadab2%2C1e47ab3c-d2a0-4a88-8cb6-18d6177492a9%2C1fb88757-24f5-4317-bc87-8c2d4dba65cd%2C1fed83a9-e10d-45a7-92e0-41da73cc76d5%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C4143f2d0-4e59-4ff6-9151-d53a0306aded%2C51198fdc-779e-4881-bc41-129ef8f11600%2C5566c919-5e24-44be-9bfd-47fab0a61957%2C753ebe2f-a6bc-4071-9791-3730e6d1b372%2C83c0a279-ff9d-4961-8012-47cc14cc45c0%2C886539ab-e031-4ec2-91ab-1ed71ee1d2a7%2C8fcdbc7a-f907-4fb7-b7c8-05823140e024%2C901f183a-8082-4b46-ba4e-027431685402%2C91fd0374-e935-49ff-8fbe-8b2e203c1730%2C9ca6fd1c-77ea-4782-be35-226dea85eb01%2Ca12a6029-0535-4ac6-bfe1-ce4f06e17c3c%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Cbf62c34e-6ea0-4b8d-b944-fbdf2ab1484a%2Cc872f2dc-a93f-4500-a134-0afdb9590570%2Ccbde045d-f1f3-4d46-b0e7-186e47102b6c%2Cd9d02f87-4085-471c-b84f-fb3a8399c683%2Ce79b92c4-98e1-49ef-a472-f57f210ca12e%2Cf457b68e-928e-453e-8ced-641c244dbf6d&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = VideoGames_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1



    def groupTV(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/television-and-home-theater?brand=06d7ec3e-8cbe-4948-9305-3dc1c15eede0%2C16595e8c-dd80-4d20-9dcb-d418eaac9e5d%2C1a489476-3c3e-4547-a6f0-9d81456f48c3%2C22e97606-1855-4ca4-97d3-88774a05e415%2C23d34b72-ea5b-464e-b1c9-092611f27b78%2C26acd6be-3782-439d-9ab5-0a1e770b4070%2C2a28bf9a-c295-4fff-8837-47b7721c3880%2C2c60a609-00d4-4ec2-a621-5b475826c676%2C3e8eaeac-fef0-4f10-9763-ae14fc8a2834%2C41044913-09b9-4635-b502-64cc3800faf5%2C4dd9e58f-5c18-434a-bc0d-28bfe0ad5f8f%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C50b8632d-c107-4605-8602-879ac6994f97%2C559bba57-6dd8-443b-8ccc-d430742fc90c%2C56759bfc-0531-496b-814e-dbc33fa6a4b9%2C5bd5d980-ae92-4e67-ba09-cd135ad13171%2C5f6e1462-a7df-4dd5-9a62-ee1077b7ffb8%2C62d753c8-121b-45cc-b3a3-b05344c2fc45%2C70fde650-5c08-49df-b014-9121a4379144%2C716a046c-07c8-4693-b229-f75ef47e5f6c%2C7c5d2fcc-863f-47aa-8a5b-22c9cd71c5d1%2C7e4343b6-4a86-424e-97b6-ce1abf38176c%2C80da9a2d-ee03-4fbc-ad70-3d330ce92787%2C827ef3f7-aadf-46c5-85e6-c6bacfeaae0b%2C89f2031c-bce5-4455-a829-b08f98bd2168%2C8efa5611-0f81-4233-93f1-e922c8f6dc73%2C9094d5f6-2ff1-4ef4-be8a-2c69b4f1d1a8%2C99fe73a1-549c-46bc-a113-ccbf8eb73290%2C9ae360c3-e16b-4e95-a0f5-3eee76da074e%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2C9ca6fd1c-77ea-4782-be35-226dea85eb01%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Ca5d13c08-b207-4ab9-a024-53b11589513d%2Cab33b273-3c05-4d01-bd4e-a2684364b1a3%2Caf90baa3-69d5-43cb-b534-64ea28b17723%2Cb1b26138-5f3c-4679-9a4f-fbb53d9a7436%2Cb626b945-e015-44fa-8be7-a3879d0ba51f%2Cb815a10b-c465-4a24-abf0-690d0a89f99b%2Cbcd9ff16-4ec7-46d3-9931-7b58b42c34ce%2Cc2534932-01fe-474e-be29-c227b7640a47%2Cc6817c9f-0bf1-4d4e-a195-c3ed37679dde%2Ccb7a7155-63ce-4eaf-8e25-f349c892c3f9%2Ccbc369ca-101b-4f99-913b-583a4d9ca647%2Cd298a9eb-be6d-4681-a9c5-efaffcc6059b%2Cd2993075-4ae9-435b-bcc5-4fcd450254d4%2Cd9e215db-1124-44b1-aff2-0d0c5d961dee%2Ce03e26ee-7f48-48f9-aa6f-9a2234cc43f9%2Ce12ad848-bef9-4dd0-89e5-975696066c71%2Cf00c5842-d3fa-453b-b916-32294917472b%2Cf8ffed82-6c2c-407b-bef8-b33b97d70071&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img=""
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = TV_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1


    def groupMovies(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods?category=entertainment-and-media&category2=movies-and-tv&query=movies&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img=""
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Movies_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1


    def groupAppliances(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods?category=for-the-home&category2=appliances-goods&query=appliances&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img=""
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Applinces_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1


    def groupToys(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods?category=baby-kids-and-toys&category2=toys&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img=""
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Toys_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1



    def groupHome(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods?category=for-the-home&category2=art-and-home-decor&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            if "Oops" in plain_text:
                print "OOPPPS"
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []

                for link in soup.findAll('figure', {'class': 'card-ui'}):
                    img=""
                    for li in link.findAll('img', {'class': 'cui-image'}):
                        # print li
                        img = li.get('data-high-quality')
                        # print img

                    for li in link.findAll('span', {'class': 'cui-price-discount'}):
                        price = li.text.strip()
                        # prices.append(price)
                        # print "price "+li.text.strip()

                    for li in link.findAll('div', {'class': 'cui-udc-title'}):
                        title = li.text.strip()
                        # titles.append(title)
                        # print "Title "+li.text.strip()

                    for addr in link.findAll('a', {'ontouchstart': ""}):

                        address = addr.get("href")

                        # print address
                        inside_url = address
                        inside_source = requests.get(inside_url)
                        inside_plain_text = inside_source.text
                        inside_soup = BeautifulSoup(inside_plain_text, "lxml")
                        for lin in inside_soup.findAll('div', {'itemprop': 'description'}):
                            description=lin.text.strip()

                    count = 0

                    request["SNR_Price"] =price[1:]

                    request["SNR_Brand"] = "Visit site to see Brand"
                    request["SNR_Available"] = "Groupon "

                    request["SNR_Description"] = description

                    request["SNR_Title"] = title

                    if img !=None:

                        request["SNR_ImageURL"] ="https:"+ img
                    else:
                        request["SNR_ImageURL"]="https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg"
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "Visit site to see "
                    request["SNR_SKU"] = "Visit site to see "
                    request["SNR_UPC"] = "Visit site to see "
                    serializer = Smarthomes_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")

                    count += 1


