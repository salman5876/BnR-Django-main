import usproxy as usaproxy
import freeproxylist as allproxylist
import multiprocessing

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from random import shuffle
from multiprocessing.dummy import Pool as ThreadPool
from random import randint
import time;
import random
#Getting US-Proxies live
proxies=usaproxy.getProxyWorking()
#Shuffling Proxies List
random.shuffle(proxies)

proxies.append(allproxylist.getProxyWorking())
random.shuffle(proxies)

print len(proxies)
subpage=[
        "Accessories",
        "Amazon Exclusives",
        "Appliances",
        "Arts",
        "Audio Devices",
        "Automotive",
        "Cameras & Camcorders",
        "Cellphones & Accessories",
        "Clothing & Apparel",
        "Computer & Laptops",
        "Computer Hardware & Software",
        "Computer Software",
        "Deals",
        "Electronics",
        "Entertainment",
        "Fashion",
        "Furniture",
        "Gifts",
        "Grocery, Household & Pet",
        "Health & Beauty",
        "Home & Garden",
        "Jewelry & Watches",
        "Kindle & Fire Tablets",
        "Mobile Apps",
        "Movies, Music & Books",
        "Office Supplies",
        "Security",
        "Shoes",
        "Smart home & security",
        "Sports",
        "Tools",
        "Toys, Kids & Babies",
        "Uncategorized",
        "Vehicle & GPS",
        "Video Games & Consoles"
    ]
# proxies=['74.209.243.116:3128']
def run(proxy):
    option = webdriver.ChromeOptions()
    option.add_argument("incognito")
    print proxy
    option.add_argument('--proxy-server=%s' % proxy)
    option.add_argument(('user-agent=%s'%proxy))
    browser = webdriver.Chrome(executable_path='/home/brainplow123/chromedriver', chrome_options=option)
    scrollpoint = (randint(05, 1000));


    sub_page_to_go = (randint(00, 28));

    waitTimeonPage=randint(0,58)

    stayTimeonPage=randint(0,90)

    #Getting Page
    browser.get("https://www.shopnroar.com/")

    #Scroll Randomly
    browser.execute_script("window.scrollTo(0, "+str(scrollpoint)+")")

    #Stay sometime on page & Click
    openpage=randint(0,len(subpage))
    time.sleep(waitTimeonPage)
    try:

        link = browser.find_element_by_link_text(subpage[sub_page_to_go])
        link.click()
        time.sleep(320);
        sub_page_to_go = (randint(00, 28));

        link = browser.find_element_by_link_text(subpage[sub_page_to_go])

        link.click()


    except:

        time.sleep(stayTimeonPage);

    # Wait 20 seconds for page to load
    timeout = 1000000
    try:
        WebDriverWait(browser, timeout)
        time.sleep(5)

        # browser.quit()
    except TimeoutException:
        print("Timed out waiting for page to load")
        # browser.quit()

for proxy in proxies:
    # run(proxy)
    time.sleep(60)


    pool = ThreadPool(3*4)

    results = pool.map(run, proxies)

    pool.close()
    pool.join()



#
#
# from tbselenium.tbdriver import TorBrowserDriver
# with TorBrowserDriver("/home/brainplow123/tor-browser_en-US/") as driver:
#     driver.get('https://www.whatismyipaddresslocation.com/')
