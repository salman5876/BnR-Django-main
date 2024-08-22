def clean_header_footer(soup):
    [s.extract() for s in soup('script')]
    [s.extract() for s in soup('footer')]
    [s.extract() for s in soup('head')]
    [s.extract() for s in soup('aside')]
    [s.extract() for s in soup('nav')]
    [s.extract() for s in soup('iframe')]
    [s.extract() for s in soup('svg')]
    return soup

def clean_sidebar_meta_widgets(soup):
    try:
        soup.find('div', {'id': 'sidebar-wrapper'}).decompose()
    except:
        print "no side bar"
    try:
        # soup.find('div', id="secondary").decompose()
        # soup.find('div', {'class':"widget-area"}).decompose()
        soup.find('div', class_='widget-area').decompose()
    except:
        print "no widget"

    try:
        # soup.find('div', id="secondary").decompose()
        # soup.find('div', {'class':"widget-area"}).decompose()
        soup.find('div', id='post-meta').decompose()
        # soup.select('div[class*="meta"]').decompose()
    except:
        print "no meta"

    return soup




import requests
from bs4 import BeautifulSoup



head_tags=['h1','h2','h3','h4','h5']
# url = 'http://kblog.lunchboxbunch.com/'
# url = 'https://www.mommypotamus.com/'
# url = 'https://familyfoodllc.com/blog/tips-for-smart-grocery-shopping/'
url = 'https://www.dexafit.com/blog2/top-20-health-and-fitness-blogs-2018'
source = requests.get(url)
plain_text = source.text
soup = BeautifulSoup(plain_text, "lxml")
soup= soup.body

titles=[]

soup=clean_header_footer(soup);
soup=clean_sidebar_meta_widgets(soup);

# print soup

try:
    for title in soup.findAll('h1'):
        if(len(title.text)>20):
            print(title.text)
            titles.append(title.text)
        else:
            print "empty"

    # print(soup.find('h1').text)
except:
    for title in soup.findAll('h2'):
        if(len(title.text)>20):
            print(title.text)
            titles.append(title.text)
        else:
            print "empty"


print(titles)

try:
    print("trying")
    body=soup.select('div[class*="body"]')
    text=body.p.text
    print(text)

except:

    try:
        for body in soup.select('div[class*="content"]'):
            print body
            # for para in soup.findAll('p'):
            #     print(para.text)
            break
    except:
        print("No content")

# articles=soup.findAll('article')
# print   articles






# for article in articles:
#     print(article)
# print soup.get_text()

# child="";
#
# def getparent(child):
#     return child.parent
# # print soup.get_text()
#
# for tag in head_tags:
#     # try:
#         for elem in soup.findAll(tag):
#             print tag+" : "+elem.text
#
#             elem=getparent(elem)
#
#             while elem.p is None:
#                 elem=getparent(elem)
#
#             print elem.p
#
#             break
#             # while elem.p is None:
#             #      getparent(elem)
#
#             # print elem.parent.parent.find('p').text
#
#             # break
#             # print elem.find(elem.parent.parent.name)
#             # print elem.child.name
#         # break
#     # except:
#     #     continue
# #


