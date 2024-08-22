from .serializers import Wearable_Serializer
import requests
import json
import unicodedata
from rest_framework.response import Response  # to send specific response
from rest_framework import status
from bs4 import BeautifulSoup
import time
baseAddress = "http://localhost:8000/"


class GroupOnAPI():
    def groupWearable(self, request):

        flag = True
        page = 1
        while flag == True:
            time.sleep(3)
            url = 'https://www.groupon.com/goods/wearable-technology?brand=119d26b8-2afe-4494-bbd6-702f5c7fee6c%2C298dfbcc-9737-42a1-b79e-b8820ad55737%2C2badc5e4-b30d-4ef2-8510-5777a95b40b1%2C32f7210d-2ea7-498d-a2a9-5716a8e83ce2%2C4be23845-9268-48ac-809f-fc1324f36a8f%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C6a886149-f219-4423-9978-79d9a274088e%2C8c08fd0c-e9b5-4900-9878-a3d53cfb5bf8%2C9a2a5ef7-a244-4851-8960-e36246e38eea%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2C9e1e4822-b9a6-4367-a947-1f6afa68dc21%2Ca1957946-766d-4cf5-b446-af7476ed302a%2Ca5778cf0-3881-4d02-9ab8-20c6c5543717%2Ca6a8b9e2-f1a4-42a6-8151-0ca80f8e85b7%2Ca77185b5-b78c-423a-be8a-0fb4545a1e64%2Ca8789205-ee9d-46f2-9922-817e547d56ff%2Cb1ccee99-5a63-4dfc-81cf-6044bdabbd19%2Ccee45173-df2a-4f4d-a1f2-bd868cc9572c%2Cd19b8561-fc62-4a04-b797-e29be85c9c0c%2Cd6c85834-4d68-49bb-9934-b0170d779787%2Ce16da45a-8423-47f0-9278-dd863904a3ae%2Cec03289e-2556-4d42-b8b9-9eb395757c34%2Cf31f1916-1668-405c-bf1f-dcd04acc674e%2Cfd768008-970f-4dd1-bb48-b171429c1d1b&page='+str(page)
            source = requests.get(url)
            plain_text = source.text
            # print plain_text
            if "Oops" in plain_text:
                print "OOPPPS"
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
                    try:

                        request["SNR_Price"] = price[1:]

                        request["SNR_Brand"] = "Visit site to see Brand"
                        request["SNR_Available"] = "Groupon "

                        request["SNR_Description"] = description.decode('unicode_escape').encode('ascii', 'ignore')

                        request["SNR_Title"] = title.decode('unicode_escape').encode('ascii', 'ignore')

                        request["SNR_ImageURL"] ="https:"+ str(img)
                        request["SNR_ProductURL"] = address
                        request["SNR_ModelNo"] = "00"
                        request["SNR_SKU"] = "00"
                        request["SNR_UPC"] = "00"
                        serializer = Wearable_Serializer(data=request)
                        print("calling ")
                        print(serializer)
                        if serializer.is_valid():
                            print("---")
                            serializer.save()
                        else:
                            # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
                            print serializer.error_messages

                            print("bad json")
                    except:
                        print "error"

                    count += 1




