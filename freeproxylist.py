from time import sleep

import requests
from bs4 import BeautifulSoup


import os, django

from concurrent.futures import ProcessPoolExecutor
from requests import Timeout, ConnectionError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()



header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
req_session = requests.Session()

def getProxyWorking(ur='',visited=[],arr=False,strip=False):
    proxy_url = "https://free-proxy-list.net"
    count = 0;

    soup = getSoup(url=proxy_url)
    soup = soup.select("table#proxylisttable tbody tr")
    all_https_prox = []
    all_prox = []
    for i in soup:
        ip, port, code, _, _, _, https, _ = [j.text for j in i.find_all("td")]
        proxy = "{0}:{1}".format(ip, port)
        print proxy
        count=count+1;
        print count
        all_prox.append(proxy)
        if https.lower() == "yes":
            if proxy not in visited:
                all_https_prox.append((proxy))
                # print all_https_prox
    if arr:
        all_data = []
        with ProcessPoolExecutor(max_workers=8) as executor:
            future = executor.map(testProxy, all_https_prox, chunksize=3)
            for temp in future:
                if temp:
                    if strip:
                        temp = temp["http"]
                    all_data.append(temp)
            executor.shutdown(wait=True)

        return all_data
    else:
        for dt in all_https_prox:
                temp = testProxy(dt)
                if temp:
                    if strip:
                        temp = temp["http"]

                    return temp

    return all_prox


def testProxy(data):
    proxy = data

    proxies ={
        "http": proxy,
        "https":proxy
    }
    try:
        a= requests.get(proxies=proxies,timeout=15,headers=header)
        if a.status_code ==200:
            return proxies
    except Exception as e:
        pass

    return False




def getSoup(data="",url=False,proxy={},cookies={}):
    if url:
        data = getRawData(url=url,proxy=proxy,cookies=cookies)

    return BeautifulSoup(data,"lxml")



def getRawData(url,data={},headers="Waryam",post=False,json=False,timeout=50,proxy=False,cookies={},verify=True,obj=False,robot="automated access",retry_code=[]):
    if headers=="Waryam":
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }

    req = req_session.get
    if post:
        req = req_session.post

    while True:
        try:
            print "Getting Data From {0}".format(url)
            if proxy:
                temp = req(url,data=data,headers=headers,timeout=timeout,proxies=proxy,verify=verify,cookies=cookies)
            else:
                temp = req(url,data=data,headers=headers,timeout=timeout,verify=verify,cookies=cookies)

            if obj:
                return temp

            if robot in temp.text:
                sleep(15)
                continue
            if temp.status_code == 200:


                data = temp
                if json:
                    return data.json()
                return data.text
            else:
                if temp.status_code in retry_code:
                    sleep(5)
                    continue

                raise Exception("Some Error Occured, Bad Status Code ({0})".format(temp.status_code))

        except Timeout:
            print "Timeout: Failed Getting Data From {0}, Retrying".format(url)
        except ConnectionError:
            print "ConnectionError: Failed Getting Data From {0}, Retrying".format(url)

        except Exception as e:
            raise e

#
getProxyWorking()