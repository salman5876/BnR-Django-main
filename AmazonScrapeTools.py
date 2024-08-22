import re
import requests
from selenium import webdriver
from time import sleep
from requests import Timeout, ConnectionError
from bs4 import BeautifulSoup
from urllib.parse import urlparse,urljoin
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer, DailyDeals_Serializer,AmazonURLs_Serializer
from products.models import AmazonURLs, AmazonProxies
from django.db.models.query_utils import Q
from django.db.models import Min
import json
from CatMap import cap_dict
from selenium.common.exceptions import TimeoutException
from concurrent.futures import ProcessPoolExecutor
from pyvirtualdisplay import Display
# from TorCtl import TorCtl
# import socket
# import socks
# ip='127.0.0.1' # change your proxy's ip
# port = 9150 # change your proxy's port
# socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
# socket.socket = socks.socksocket
# __originalSocket = socket.socket


class ScrapeTools(object):
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    # }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36',
    }
    count = 0
    driver =''
    display=''
    def __init__(self,poolno):
        self.poolno = poolno
        self.proxy = self.getProxyWorking()
        # self.driver = self.getWebDriver(proxy=self.proxy)
        # self.driver = self.getWebDriver()

    # def getWebDriver(self,proxy):
    def getScrapeData(self,min_range,max_range):
        data = AmazonURLs.objects.filter(status_scrape=False).order_by('id').filter(id__range=(min_range,max_range))
        # .filter(id__range=(10,20))
        # [min_range:max_range]
        serializer = AmazonURLs_Serializer(data,many=True)
        return serializer.data
    def changeStatus(self,value):
        que = Q(Cat=value[0], SubCat=value[1], url=value[2])
        data = AmazonURLs.objects.get(que)
        data.status = True
        data.save()
        return data
    def phantomJSBrowser(self,proxy):

        if proxy:
            proxy1 = proxy['http']
            args = ['--proxy={}'.format(proxy1, '--proxy-type=socks5')]
            browser = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-linux-x86_64/bin/phantomjs', service_args=args)
        else:
            browser = webdriver.PhantomJS(executable_path='./phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        browser.maximize_window()
        return browser
    def getWebDriver(self,proxy):

        self.display = Display(visible=0, size=(1024, 768))
        self.display.start()

        if proxy:
            proxy1 = proxy['http']
            options = webdriver.ChromeOptions()
            options.add_argument('--proxy-server=%s' % proxy1)
            options.add_argument('--disable-notifications')
            options.add_argument('--no-sandbox')
        else:
            options = webdriver.ChromeOptions()
            # options.add_argument('--proxy-server=%s' % proxy1)
            options.add_argument('--disable-notifications')
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
        return driver

    # def newId(self):
    #     __originalSocket = socket.socket
    #     ''' Clean circuit switcher
    #
    #     Restores socket to original system value.
    #     Calls TOR control socket and closes it
    #     Replaces system socket with socksified socket
    #     '''
    #     socket.socket = __originalSocket
    #     conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="123")
    #     TorCtl.Connection.send_signal(conn, "NEWNYM")
    #     conn.close()
    #     socket.socket = socks.socksocket

    def getRawData(self,url,session = requests.Session(),data={}, post=False, json=False, timeout=300, proxy=False,cookies={'skin': 'noskin'},
                   verify=True, obj=False, robot="automated access", retry_code=[]):
        # if headers == "Waryam":
        #     headers = {
        #         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        #     }
        #
        # req = session.get
        # if post:
        #     req = session.post

        # cookies = {
        #     'x-wl-uid': '1fVJNhMtzM+co0gxYI4RVRmDAG1F31fH0gPdUi/RpooRvbP3T6shj59EIqI6vnXQWeFe1eiaedAY=',
        #     'session-id-time': '2082787201l',
        #     'session-id': '139-1471257-5234354',
        #     'csm-hit': 'tb:s-AN4B58JED3ZWF1NA35CW|1549280193920&t:1549280196009&adb:adblk_no',
        #     'ubid-main': '132-4863831-2629356',
        #     'session-token': 'tvWjRYzJuH5rluGrdPP3O3FeBKD9kfdzJsxI7oe/laQMBq9vGsc7wxL737h8bCboE5PD2nrue656ELWTLL66ttqiNAaNGm2joXCuYqDT4mVZLzJEpVACcHVMbdzwQNSPW6FYGqoO4S1C9L3JVngVDtMIjBuyQ1OgMq++E9ehB7WlLtN9EIOZXB6SgPI51Q9s',
        #     'i18n-prefs': 'USD',
        #     'skin': 'noskin',
        # }
        while True:
            try:
                print ("Getting Data From {0}".format(url))

                self.driver.get(url)


                # temp = req(url, data=data, headers=self.headers,timeout=timeout,proxies=self.proxy, verify=verify,cookies = cookies)

                # if obj:
                #     return temp

                if robot in self.driver.page_source:

                    print ('Robot')
                    # proo = AmazonProxies.objects.get(proxy=self.proxy)
                    # proo.delete()
                    # sleep(300)
                    self.driver.quit()
                    self.display.stop()
                    # self.prox = False
                    # while True:
                    self.proxy = self.getProxyWorking()
                    # self.driver = self.getWebDriver(proxy=self.proxy)
                    # self.proxy = self.getProxyWorking(ur=url)
                    # session = requests.Session()
                    # req = session.get
                    # if post:
                    #     req = session.post
                            # break
                    # sleep(300)
                    # self.proxy = self.getProxyWorking()
                    continue
                # if temp.status_code == 200:
                if 'images-na.ssl-images-amazon.com' in self.driver.page_source:
                    return self.driver.page_source
                else:
                    # proo = AmazonProxies.objects.get(proxy=self.proxy)
                    # proo.delete()
                    self.driver.quit()
                    self.display.stop()
                    self.proxy = self.getProxyWorking()
                    # self.driver = self.getWebDriver(proxy=self.proxy)
                    continue
                # data = temp
                # if json:
                #     return data.json()

                # else:
                #     if temp.status_code in retry_code:
                #         self.proxy = self.getProxyWorking(ur=url)
                #         # sleep(300)
                #         print 'StatusCode'
                #         #
                #         continue

                    # raise Exception("Some Error Occured, Bad Status Code ({0})".format(temp.status_code))

            # except Timeout:
            #     print "Timeout: Failed Getting Data From {0}, Retrying".format(url)
            #     self.proxy = self.getProxyWorking(ur=url)
            except TimeoutException:
                # proo = AmazonProxies.objects.get(proxy=self.proxy)
                # proo.delete()
                self.driver.quit()
                self.display.stop()
                self.proxy = self.getProxyWorking()
                # self.driver = self.getWebDriver(proxy=self.proxy)
                continue
            # except ConnectionError:
            #     print "ConnectionError: Failed Getting Data From {0}, Retrying".format(url)
            #     self.proxy = self.getProxyWorking(ur=url)

            except Exception as e:
                print (e)
                # sleep(300)
                self.driver.quit()
                self.display.stop()
                self.proxy = self.getProxyWorking()
                # self.driver = self.getWebDriver(proxy=self.proxy)

    def getSoup(self,data="", url=False):
        if url:
            data = self.getRawData(url=url)

        return BeautifulSoup(data, "lxml")

    def testProxy(self,data):
        proxy, ur = data
        robot = "automated access"

        proxies = {
            "http": proxy,
            "https": proxy
        }
        try:
            a = requests.get(url=ur, proxies=proxies, timeout=100, headers=self.headers)
            if robot in a.text:
                print ('Robot')
                return False
            if a.status_code == 200:
                return proxies
        except Exception as e:
            pass

        return False

    def getUsProx(self,url):
        while True:
            try:
                self.driver = self.getWebDriver(proxy=False)
                print ('Getting Proxy for {0}'.format(url))
                self.driver.get(url)
                button = self.driver.find_elements_by_css_selector(".hx.ui-state-default")
                self.driver.implicitly_wait(10)
                button[0].click()
                self.driver.implicitly_wait(10)
                button[0].click()
                try:
                    soupp = BeautifulSoup(self.driver.page_source,'lxml')
                    self.driver.quit()
                    self.display.stop()
                    print ('proxy page success')
                    return soupp
                except Exception as e:
                    print ('Proxy Inner Except')
                    print (e)
                    self.driver.quit()
                    self.display.stop()
                    # sleep(300)
                    continue
            except Exception as e:
                print ('Proxy Outer Except')
                print (e)
                self.driver.quit()
                self.display.stop()

    def getProxyWorking(self,ur='https://www.amazon.com',visited=[], proxList=[], strip=False):
        proxy_url = "https://www.us-proxy.org/"
        robot = "automated access"
        # proo = AmazonProxies.objects.order_by('count')[0]
        # proxies = proo.proxy
        # proo.count +=1
        # proo.save()
        # self.driver = self.getWebDriver(proxy=proxies)
        # return proxies
        while True:
            print ('Going to proxy page')
            soup = self.getUsProx(url=proxy_url)
            soup = soup.select("table#proxylisttable tbody tr")
            all_prox = []
            for i in soup:
                ip, port, code, _, _, _, https, _ = [j.text for j in i.find_all("td")]
                proxy = "{0}:{1}".format(ip, port)

                if https.lower() == "yes":
                    if proxy not in visited:
                        all_prox.append((proxy, ur))
            if len(all_prox) == 0:
                visited=[]
            for dt in all_prox:
                proxies = {"http": dt[0],"https": dt[0]}
                self.driver = self.getWebDriver(proxy=proxies)
                visited.append(proxies['http'])
                try:
                    print ('proxing')
                    self.driver.get(ur)
                    print ('proxing url success')
                    if robot in self.driver.page_source:
                        self.driver.quit()
                        self.display.stop()
                        print ('Robot for url {0}'.format(ur))
                        # sleep(600)
                        continue

                        # proxyList.append(proxies)
                        # if len(proxyList) == proxList:
                    if 'images-na.ssl-images-amazon.com' in self.driver.page_source:
                        print ('proxing success')
                        return proxies
                    else:
                        self.driver.quit()
                        self.display.stop()
                        # sleep(300)
                except Exception as e:
                    print ('Exception is {0}'.format(e))
                    self.driver.quit()
                    self.display.stop()
                    # sleep(300)
                    continue

            continue
                    # temp = self.testProxy(dt)
                    # if temp:
                    #     if strip:
                    #         temp = temp["http"]
                    #     visited.append(temp['http'])
                    #     return temp

    def getAbsUrl(self,base, part):
        return urljoin(base, part)

    def patSearch(self,pat, string):
        return next(re.finditer(pat, string))

    def data_send(self,request):
        # d = json.dumps(request)
        # d = binascii.hexlify(d.encode('utf8'))
        # d= 'python dcommit.py "{0}"'.format(d)
        # subprocess.call(d,shell=True)
        # return

        try:
            serializer = AllProducts_Serializer(data=request)

            if serializer.is_valid():
                self.count = self.count + 1
                print("INSERT",self.count)
                serializer.save()
            else:
                self.count = self.count + 1
                print (serializer.errors)
                print("bad json",self.count)
        except Exception as e:
            try:
                with open("exceptions.txt", "a") as w:
                    w.write(str(e) + " " + json.dumps(request) + "\n")
            except:
                pass

    def get_data_pro(self,dt):

        for request in dt:
            try:
                request["SNR_ImageURL"] = str(request["SNR_ImageURL"])
                request["SNR_Title"] = str(request["SNR_Title"])
                request["SNR_ProductURL"] = str(request["SNR_ProductURL"])
                request["SNR_Description"] = str(request["SNR_Description"])
                item = request["SNR_Category"] + ',' + request["SNR_SubCategory"]
                item = item.capitalize()
                request["SNR_MainCatID"] = cap_dict[item][2]
                request["SNR_CatID"] = cap_dict[item][0]
                request["SNR_SubCatID"] = cap_dict[item][1]
            except:
                pass
            yield request

    def commit_data(self,data, batch_size=2000, par=True):
        all_data = []
        c = 0
        # pool = ThreadPool(multiprocessing.cpu_count() * 32)
        # results = pool.map(data_send, get_data(data))
        # pool.close()
        # pool.join()
        for i in self.get_data_pro(data):
            self.data_send(i)

    def get_data_deal(self,dt):

        for request in dt:
            try:
                request["SNR_ImageURL"] = str(request["SNR_ImageURL"])
                request["SNR_Title"] = str(request["SNR_Title"])
                request["SNR_ProductURL"] = str(request["SNR_ProductURL"])
            except:
                pass
            yield request

    def dealdata(self,data):

        for i in self.get_data_deal(data):
            self.commitdeal(i)

    def commitdeal(self,requests):

        serializer = DailyDeals_Serializer(data=requests)

        try:
            if serializer.is_valid():
                print("---")
                print (requests)
                serializer.save()
            else:
                print (serializer.errors)
                print (requests)
                print("bad json")
        except Exception as e:
            print ("Error")