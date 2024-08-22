import bottlenose
import json
import xmltodict

amazon = bottlenose.Amazon('AKIAJYH5LPTVAMBU6NOQ', 'DfGaLxsy9ftS/672f0VxCWgoXecj3LRxNoqLMNPA', 'mobilea0fe6ba-20')
response = amazon.ItemSearch(Keywords="NIKE Air Men's More Uptempo  PRM Light Brown AA4060-200", SearchIndex="All",ResponseGroup='ItemAttributes,Images,Large', limit=1000,)
# print(response)

# f= open("response.txt","w+")
# f.write(response)
# f.close()
response = json.dumps(xmltodict.parse(response), indent=4)
response=json.loads(response)
# print response['ItemSearchResponse']['Items']['Item']

for item in response['ItemSearchResponse']['Items']['Item']:
    print(item['ItemAttributes']['Title'])
    print(item['ItemAttributes']['Binding'])
    print(item['ItemAttributes']['ListPrice']['FormattedPrice'][1:])
    try:
        print(item['ItemAttributes']['Brand'])
    except:
        print "No Brand"
    try:
        print(item['ItemAttributes']['Model'])
    except:
        print "No Model"
    try:
        print(item['ItemAttributes']['UPC'])
    except:
        print "0000"

    try:
        print(item['ItemAttributes']['Feature'][0])

    except:
        print "Visit site to see description"


    print(item['DetailPageURL'])
    print(item['ASIN'])

    try:
        print ['MediumImage']['URL']
    except:
        try:
            for img in (item['ImageSets']['ImageSet']):
                print img['MediumImage']['URL']
                break
        except:
            print item['ImageSets']['ImageSet']['MediumImage']['URL']







# import random
#
# import requests
# from bs4 import BeautifulSoup
# import urllib
#
# query="nike airman shoes"
# query=query.replace(" ","+")
# url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+query
# source = requests.get(url)
# plain_text = source.text
# print plain_text
# soup = BeautifulSoup(plain_text, "lxml")
#
# items=[]
#
#
# # cat = soup.find('ul', {'class':'srp-refine__category__list'})
# # for link in soup.findAll('li', {'class': 's-item'}):
# #     # print link
# #     img=link.find('img').get('src')
# #     if 'gif' in img:
# #         img = link.find('img').get('data-src')
# #
# #     print img
# #     print link.find('h3',{'class':'s-item__title'}).text
# #     request = {}
# #     # try:
# #     #     request["SNR_ProductURL"] = link.find('a',{'class':'s-item__link'}).get('href')
# #     #     request["SNR_Title"] =link.find('h3',{'class':'s-item__title'}).text
# #     #     request["SNR_Description"] = "Visit site to see description"
# #     #     request["SNR_Price"] = link.find('span',{'class':'s-item__price'}).text[1:]
# #     #     request["SNR_CustomerReviews"] = 0.0
# #     #     request["SNR_PriceBefore"] = -1
# #     #
# #     #     request["SNR_Category"] = cat.findNext('li',{'class':'srp-refine__category__item'}).text
# #     #     request["SNR_Available"] = "Ebay"
# #     #
# #     #     request["SNR_ModelNo"] = "00"
# #     #     request["SNR_UPC"] = "00"
# #     #
# #     #     request["SNR_SubCategory"] =cat.findNext('li',{'class':'srp-refine__category__item'}).text
# #     #     request["SNR_Condition"] = "00"
# #     #     request["SNR_ImageURL"] =link.find('img',{'class':'s-item__image-img'}).get('data-src')
# #     #     request["SNR_SKU"] = "EB" + str(random.randint(1,1111111))
# #     #     items.append(request)
# #
# #     # except:
# #     #     continue
# #
# # print items
# #
# #
