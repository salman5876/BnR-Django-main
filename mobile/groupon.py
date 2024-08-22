from .serializer import Mobile_Serializer
import requests
import json
import unicodedata
from rest_framework.response import Response  # to send specific response
from rest_framework import status
from bs4 import BeautifulSoup
import time
baseAddress = "http://localhost:8000/"


class GroupOnAPI():
    def groupPhones(self, request):

        flag = True
        page = 1
        while flag == True:
            time.sleep(3)
            url = 'https://www.groupon.com/goods/cell-phones-and-accessories?brand=119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C14684a8d-4f36-4775-8d8d-fd04dbc952fc%2C215b2a94-2af4-487a-bb8c-c3ac8c5c1daa%2C35d18f3a-8ac7-49c7-b555-5c13181343f3%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C43f785c7-da5f-4602-b89c-53793fa22251%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C51fb58f7-c33d-4d77-96c8-c4c0dac9e4f1%2C5f6e1462-a7df-4dd5-9a62-ee1077b7ffb8%2C6262bb0d-1697-4b5a-83a7-cc0f8655fd2f%2C965b4979-61eb-4150-a63e-6a55b150c70c%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2Ca0e35859-9583-4086-9146-cd504aab2703%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Ca8f436ea-5888-4c80-9bd6-dd35dda4d48e%2Cc1a9bca5-c09e-4555-bba6-672a22046ac1%2Cc8da91a3-e3d6-4a45-ac3e-615d12921acb%2Cd0373173-ec82-450d-ae89-2dd7b7149c0f%2Cd19ef46c-4917-453b-9378-ad3494e56b69%2Cd785b3db-ea1a-4b74-8742-8e085589e527%2Cdb89a50c-3579-4a71-91a7-c2c4daa93ecb%2Ce73aec2d-a484-4d8d-bf1a-842b694e3feb%2Cecb805e3-1ff5-4196-87ca-d33e2001e2e7%2Cf4555cbf-e4f6-411c-8475-fd85b406b302%2Cf457b68e-928e-453e-8ced-641c244dbf6d%2Cf7ab9ef7-85a1-4e47-8532-eccc7b369918&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            print(plain_text)
            if "Oops" in plain_text:
                print("OOPPPS")
                flag = False
            else:
                page += 1

                soup = BeautifulSoup(plain_text, "lxml")


                images = []
                prices = []
                titles = []
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

                    request["SNR_ImageURL"] ="https:"+ str(img)
                    request["SNR_ProductURL"] = address
                    request["SNR_ModelNo"] = "00"
                    request["SNR_SKU"] = "00"
                    request["SNR_UPC"] = "00"
                    serializer = Mobile_Serializer(data=request)
                    print("calling ")
                    print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
                        print(serializer.error_messages)

                        print("bad json")

                    count += 1




