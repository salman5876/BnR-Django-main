import re
from time import sleep

from selenium import webdriver
from datetime import datetime, timedelta
from requests import Timeout, ConnectionError
from bs4 import BeautifulSoup
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer, DailyDeals_Serializer,AmazonURLs_Serializer,AmazonProxies_Serializer
from products.models import AmazonURLs, AmazonProxies
from django.db.models.query_utils import Q
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display


def getWebDriver(proxy):
    while True:
        try:
            display = Display(visible=0, size=(1024, 768))
            display.start()

            if proxy:
                proxy1 = proxy['http']
                options = webdriver.ChromeOptions()
                options.add_argument('--proxy-server=%s' % proxy1)
                options.add_argument('--disable-notifications')
                options.add_argument('--no-sandbox')
            else:
                options = webdriver.ChromeOptions()
                options.add_argument('--disable-notifications')
                # options.add_argument('--disable-dev-shm-usage')
                # options.add_argument('--shm-size=2g')
                options.add_argument('--no-sandbox')

            # chrome_options = webdriver.ChromeOptions()
            # chrome_options.add_argument('--proxy-server=%s' % self.proxy1)
            # chrome_options.add_argument("--headless")  # Runs Chrome in headless mode.
            # chrome_options.add_argument('--no-sandbox')  # # Bypass OS security model
            # chrome_options.add_argument('start-maximized')
            # chrome_options.add_argument('disable-infobars')
            # chrome_options.add_argument("--disable-extensions")

            # options = webdriver.ChromeOptions()
            # options.add_argument('--proxy-server=%s' % proxy1)
            # options.add_argument('--disable-notifications')
            # options.add_argument('--no-sandbox')
            driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=options)
            # driver = webdriver.Chrome(executable_path="/home/brainplow123/Desktop/backend/shopnroar-backend-rev-updated/chromedriver", chrome_options=options)

            # driver = webdriver.Chrome(executable_path="./chromedriver",
            #                           chrome_options=chrome_options)
            return (driver,display)
        except:
            sleep(10)
            pass

def getUsProx(n,url,driver,display):
    while True:
        try:
            print ('Getting Proxy for {0}'.format(url))
            driver.get(url)
            button = driver.find_elements_by_css_selector(".hx.ui-state-default")
            driver.implicitly_wait(10)
            button[0].click()
            driver.implicitly_wait(10)
            button[0].click()
            if n ==2:
                page = driver.find_element_by_link_text('Next')
                page.click()
            elif n==3:
                page = driver.find_element_by_link_text('Next')
                driver.implicitly_wait(10)
                page.click()
                page = driver.find_element_by_link_text('Next')
                driver.implicitly_wait(10)
                page.click()
            soupp = BeautifulSoup(driver.page_source, 'lxml')
            # driver.quit()
            # display.stop()
            print('proxy page success')
            return soupp
        except:
            pass


def getProxyWorking(ur='https://www.amazon.com/b?node=16225007011&pf_rd_p=3fec1ea5-b2b9-464b-b16f-5031601225b9&pf_rd_r=Z2W4C0YE6VG9X2Z6T1PF', visited=[], proxList=[], strip=False):
    proxy_url = "https://www.us-proxy.org/"
    robot = "automated access"
    proxy_list = []
    n=0
    while True:
        n+=1
        print ('Going to proxy page')
        if n == 1:
            driver1, display1 = getWebDriver(proxy=False)
        while True:
            try:
                soup = getUsProx(n,proxy_url,driver1,display1)
                if n == 2:
                    driver1.quit()
                    display1.stop()
                break
            except Exception as e:
                print(e)
        soup = soup.select("table#proxylisttable tbody tr")
        all_prox = []
        for i in soup:
            ip, port, code, _, _, _, https, _ = [j.text for j in i.find_all("td")]
            proxy = "{0}:{1}".format(ip, port)

            if https.lower() == "yes":
                all_prox.append((proxy, ur))
        for index, dt in enumerate(all_prox):
            proxies = {"http": dt[0], "https": dt[0]}
            driver,display = getWebDriver(proxy=proxies)
            try:
                print ('proxing')
                driver.get(ur)
                print ('proxing url success')
                if robot in driver.page_source:
                    driver.quit()
                    display.stop()
                    print ('Robot for url {0}'.format(ur))
                    # sleep(600)
                    continue

                    # proxyList.append(proxies)
                    # if len(proxyList) == proxList:
                if 'images-na.ssl-images-amazon.com' in driver.page_source:
                    driver.quit()
                    display.stop()
                    yield proxies['http']
                else:
                    driver.quit()
                    display.stop()
                    # sleep(300)

            except TimeoutException:
                driver.quit()
                display.stop()
            except Exception as e:
                print ('Exception is {0}'.format(e))
                driver.quit()
                display.stop()
                # sleep(300)
                continue

        if n == 2:
            break


        # return proxy_list

if __name__ == '__main__':
    while True:
        time_threshold1 = datetime.now() - timedelta(hours=2)
        results = AmazonProxies.objects.filter(date__lt=time_threshold1)
        results.delete()

        for i in getProxyWorking():
            request = {'proxy': i }
            serializer = AmazonProxies_Serializer(data=request)
            # while True:
            if serializer.is_valid():
                serializer.save()
                print ('INSERT')
                    # break
            else:
                print (serializer.errors)
                print ('bad json')
