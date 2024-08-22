__author__ = 'Amad'
import requests
from bs4 import BeautifulSoup
from .serializers import Laptop_Serializer
import unicodedata

class ATNT():
    def getLaptops(self,request):
        url='https://www.att.com/shop/wireless/devices/tablets.html'
        source=requests.get(url)
        plain_text=source.text
        soup= BeautifulSoup(plain_text,"lxml")
        titles=[]
        images=[]
        prooductlinks=[]
        prices=[]
        sku=[]
        descriptons=[]
        ratinglink=[]

        for link in soup.findAll('a',{'class':'titleURLchng'}):


            lin="https://www.att.com"+link.get('href')
            prooductlinks.append(lin)
            title= link.string
            SKU=link.get('data-cskuid')
            sku.append(SKU)

            titles.append(title)

        for link in soup.findAll('img',{'class':'inStockOpacity'}  ):

            img=link.get('src')

            images.append(img)

        for link in soup.findAll('div',{'class':'list-description'}  ):

            des=link.get_text()
            descriptons.append(des)

        for l in soup.findAll('div',{'class':'list-priceInfo'}):

            price=l.get_text()
            # print price
            prices.append(price)

        for link in soup.findAll('a',{'class':'clickStreamSingleItem rtngURLchng'}):


            lin="https://www.att.com"+link.get('href')
            ratinglink.append(lin)


        count=0;
        for var in titles:
        # print(titles[count]+"   "+str(sku[count]))
            print(sku[count])
            for ex in soup.findAll('img',{'id':'image-'+str(sku[count])}  ):

                img=ex.get('src')

                images.append(img)

                print(img)

        for var in descriptons:


            desc=unicodedata.normalize('NFKD', var).encode('ascii','ignore')
            desc=desc.strip()
            title=unicodedata.normalize('NFKD', titles[count]).encode('ascii','ignore')
          #  skuu=unicodedata.normalize('NFKD', sku[count]).encode('ascii','ignore')
            prc=unicodedata.normalize('NFKD', prices[count]).encode('ascii','ignore')

            #print(desc)

            title=title.strip()
            prc=prc.strip()

            #print(title)




            # print titles[count]
            #
            # print(titles[count]+"   "+str(sku[count]))
            # cell = unicode(descriptons[count]).replace("\r", " ").replace("\n", " ").replace("\t", '').replace("\"", "")
            #
            #
            # print(str(cell))
            prc=prc.strip()
            print(prc)
            # print(images[count])
            request["SNR_Price"]=prc[1:-4]

            request["SNR_Brand"]="00"
            request["SNR_Available"]="AT&T"
            request["SNR_Description"]=desc
            request["SNR_Title"]=title
            request["SNR_ImageURL"]=images[count]
            request["SNR_ProductURL"]=prooductlinks[count]
            request["SNR_ModelNo"]=title
            request["SNR_SKU"]="AT"+str(sku[count])
            request["SNR_UPC"]="00"
            # request["SNR_ReviewLink"]=requests[count]

            serializer = Laptop_Serializer(data=request)
            print("bestbuy calling")
            print(serializer)
            if serializer.is_valid():
                print("---")
                serializer.save()
            else:
                print("bad json")


            count=count+1
