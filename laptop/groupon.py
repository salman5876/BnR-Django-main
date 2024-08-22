from .serializers import Laptop_Serializer
import requests
import json
import unicodedata
from rest_framework.response import Response  # to send specific response
from rest_framework import status
from bs4 import BeautifulSoup

baseAddress = "http://localhost:8000/"


class GroupOnAPI():
    def groupLaptop(self, request):

        flag = True
        page = 1
        while flag == True:

            url = 'https://www.groupon.com/goods/computers-and-tablets?brand=109e8002-7631-45e8-a2cb-9b497d982571%2C14684a8d-4f36-4775-8d8d-fd04dbc952fc%2C1f27b9c3-dfb0-46c7-8c80-a6c38b8a4dfe%2C23d34b72-ea5b-464e-b1c9-092611f27b78%2C26acd6be-3782-439d-9ab5-0a1e770b4070%2C3d942c1c-a47b-412d-a46c-45c9f191e401%2C3f05c849-3a3d-4bc0-a984-0f6cc2373a76%2C4af0d9e3-6b81-4467-847a-bc85eee9359e%2C4ec73a60-b91a-4287-b16a-c95b1d5ab308%2C7ac9c33c-07b3-475b-a36e-26097e70da9b%2C8528a092-0c2b-4f78-82e0-e9fa740885b7%2C890d12bc-9970-4023-b5cf-44568da216f5%2C8efa5611-0f81-4233-93f1-e922c8f6dc73%2C96280a34-9ba8-485a-bf0a-c6563199be44%2C97e52463-e2eb-4f60-9ab2-384e15051e5b%2C9bd95012-195d-4fa4-a37a-bb87a93c85c0%2Ca093638f-2739-42d2-a6d2-7f5777cda678%2Ca09a53e3-8818-4c8c-a862-04813f925f8a%2Ca4726dc4-c43c-4c4d-89cd-82321f943ff3%2Ca8f436ea-5888-4c80-9bd6-dd35dda4d48e%2Cc8da91a3-e3d6-4a45-ac3e-615d12921acb%2Ccffbd974-dd3d-45dc-ae3c-38effb51e828%2Cd2993075-4ae9-435b-bcc5-4fcd450254d4%2Ce5d7ebec-6220-45e4-b78d-97ead81cd6be%2Cf457b68e-928e-453e-8ced-641c244dbf6d&page='+str(page)
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
                    serializer = Laptop_Serializer(data=request)
                    print("calling ")
                    # print(serializer)
                    if serializer.is_valid():
                        print("---")
                        serializer.save()
                    else:
                        # return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

                        print("bad json")
                        # print serializer.error_messages
                        print serializer.errors

                    count += 1




