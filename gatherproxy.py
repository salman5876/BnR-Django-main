
import requests
from bs4 import BeautifulSoup
import urllib

url = 'http://spys.one/en/'
source = requests.get(url)
plain_text = source.text
# print(plain_text)
soup = BeautifulSoup(plain_text, "lxml")

count=0;
for link in soup.findAll('tr'):
    print(link)
    # for li in link.findAll('img'):
    #     # print li
    #     img = li.get('src')
    #     # filename
    #     urllib.urlretrieve("http:"+str(img), str(count)+".png")
    #     count=count+1;



