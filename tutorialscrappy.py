import requests
from bs4 import BeautifulSoup

url='https://www.ebay.com/urw/Samsung-Galaxy-Note-8-SM-N950F-DS-64GB-FACTORY-UNLOCKED-Maple-Gold-Orchid-Gray/product-reviews/239076646?_itm=232855971562'
source = requests.get(url)
plain_text = source.text
soup = BeautifulSoup(plain_text, "lxml")

items = []

# print soup.body

for rev in soup.findAll('div',{'class':' ebay-review-section'}):

    print rev
    print rev.find('h3',{'class':'review-item-title rvw-nowrap-spaces'}).text
    Reviews={};
    Reviews["SNR_Review_Title"]= rev.find('h3',{'class':'review-item-title rvw-nowrap-spaces'}).text
    Reviews["SNR_Review_Author"]= rev.find("a",class_="review-item-author").text
    Reviews["SNR_Review_Body"]= rev.find('p',{'class':'review-item-content rvw-wrap-spaces'}).text,
    Reviews["SNR_Review_Stars"]= int(rev.find("span",class_="star-rating").get('aria-label').split(" ")[0])
    Reviews["SNR_Review_UP"]= 1,
    Reviews["SNR_Review_Down"]= 1,
    Reviews["SNR_IS_SNR"]= True


    items.append(Reviews)


result={"F":items}
print {"results":result}