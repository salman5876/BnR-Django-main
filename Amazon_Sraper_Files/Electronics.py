from ScrapeTools import ScrapeTools
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
import re
from bs4 import BeautifulSoup

class Products(ScrapeTools):

    def __init__(self):
        super(Products,self).__init__(prox=False)

    def get_data_Textfile(self):
        data = []
        with open('AmazonElectronicsURLs.txt', 'r') as f:

            data = [i.split(',') for i in f]
            for index, j in enumerate(data):
                j[len(j) - 1] = j[len(j) - 1][:-1]
            print data

            # try:
            #     with open("testinggg.txt", "a") as w:
            #         for k in data:
            #             w.write('\''+k[0] + ',' + ','.join(k[1:-1]) + '\':' + ' [],' + "\n")
            # except Exception as e:
            #     pass

            # pool = ThreadPool(2)
            # results = pool.map(Data_Scraper, data)
            # pool.close()
            # pool.join()

            for k in data:
                self.Data_Scraper(k)

            print 'Completed'
            return data

    def scrape_data(self,soup, url):
        item_list = []
        robot = "automated access"
        is_next = True
        n = 0
        while is_next:
            n = n + 1
            is_next = False
            try:
                items_div = soup.select("ul.s-result-list li[id*=result] div.s-item-container")
            except:
                break
            for item in items_div:
                request = {}
                try:

                    link_div = item.select_one("a.s-access-detail-page")
                    pro_url = self.getAbsUrl(url, link_div["href"])
                    while True:
                        try:
                            print "Getting Data From {0}".format(pro_url)
                            self.driver.get(pro_url)

                            if robot in self.driver.page_source:

                                sleep(300)
                                # proxy = getProxyWorking()
                                continue
                            else:
                                break

                        except Exception as e:
                            raise e

                    button = self.driver.find_elements_by_css_selector(".a-button.a-button-thumbnail.a-button-toggle")
                    for data in button:
                        hover = ActionChains(self.driver).move_to_element(data)
                        hover.perform()
                        self.driver.implicitly_wait(10)
                    soup_pro = BeautifulSoup(self.driver.page_source, "lxml")
                    images = soup_pro.findAll("li", {"class": re.compile("^itemNo")})
                    ImageText = ''
                    for index, i in enumerate(images):
                        if index == 0:
                            ImageText = i.find("img")['src']
                        else:
                            ImageText = ImageText + ',' + i.find("img")['src']
                    request["SNR_ImageURL"] = ImageText
                    try:
                        brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").find("img").text
                        brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a")['href'].split('/b', 1)[
                            0].strip(
                            '/')
                    except:
                        brand = soup_pro.find("div", {"id": "bylineInfo_feature_div"}).find("a").text.strip()
                    request["SNR_Brand"] = brand
                    title = soup_pro.find("span", {"id": "productTitle"}).text.strip()
                    request["SNR_Title"] = str(title)
                    try:
                        Rating = soup_pro.find("span", {"id": "acrPopover"})['title'].split(' out', 1)[0].strip()
                    except:
                        Rating = 0
                    request["SNR_CustomerReviews"] = float(Rating)
                    request["SNR_ProductURL"] = pro_url
                    try:
                        PriceBefore = soup_pro.find('span', {'class': 'a-text-strike'}).text.strip().split('$', 1)[1]
                        PriceBefore = [i.replace(',', '') for i in PriceBefore]
                        PriceBefore = float(''.join(PriceBefore))
                    except:
                        PriceBefore = 0
                    request["SNR_PriceBefore"] = PriceBefore
                    try:
                        Price = soup_pro.find('span', {'id': 'priceblock_ourprice'}).text.strip().split('$', 1)[1]
                        Price = [i.replace(',', '') for i in Price]
                        Price = float(''.join(Price))
                    except:
                        try:
                            Price = \
                            soup_pro.find('span', {'id': 'priceblock_ourprice'}).text.split('-', 1)[0].split('$', 1)[
                                1].strip()
                            Price = [i.replace(',', '') for i in Price]
                            Price = float(''.join(Price))
                        except:
                            Price = 0
                    request["SNR_Price"] = Price

                    SKU = 'AZ' + soup_pro.find('div', {'id': 'cerberus-data-metrics'})['data-asin']
                    request["SNR_SKU"] = SKU

                    ModelNo = '00'
                    request["SNR_UPC"] = '00'
                    request["SNR_Available"] = 'Amazon'
                    request["SNR_Condition"] = '00'
                    try:
                        Information = soup_pro.findAll('th',
                                                       {'class': 'a-color-secondary a-size-base prodDetSectionEntry'})
                        Information1 = soup_pro.find('th', {
                            'class': 'a-color-secondary a-size-base prodDetSectionEntry'}).text
                        for i in Information:
                            if i.text.strip().lower() == 'item model number':
                                ModelNo = i.parent.text.split('number', 1)[1].strip()
                    except:
                        try:
                            Information = soup_pro.find('div', {'id': 'detailBullets_feature_div'})
                            Information = Information.findAll('span', {'class': 'a-text-bold'})
                            for i in Information:
                                if i.text.strip().lower() == 'item model number:':
                                    ModelNo = i.parent.text.split('number:', 1)[1].strip()
                        except:
                            pass

                    request["SNR_ModelNo"] = ModelNo

                    Description = ''
                    try:
                        Description = soup_pro.find('div', {'id': 'feature-bullets'}).find('ul')
                    except:
                        pass

                    request["SNR_Description"] = str(Description)

                    yield request


                except NoSuchElementException as e:
                    print e

                except ElementNotVisibleException as r:
                    print r

                except Exception as e:
                    pass

            if n == 10:
                break

            try:
                next_div = soup.select_one("a#pagnNextLink")["href"]
            except:
                break

            if next_div:
                url = self.getAbsUrl(url, next_div)
                # ProxyTimeTest()
                raw = self.getRawData(url)
                if raw == None:
                    continue
                if "did not match any products" not in raw:
                    soup = self.get_post_soup(self.getSoup(raw))
                    is_next = True

    def get_data_all(self,dt, cat, subcat):
        for request in dt:
            request["SNR_Category"] = cat
            request["SNR_SubCategory"] = subcat
            yield request

    def get_post_soup(self,soup):
        temp = soup.select_one("div#rightResultsATF")
        if not temp:
            temp = soup.select_one("div[id*=search-results]")

        return temp

    def Data_Scraper(self,data):
        print ','.join(data[1:-1])
        # ProxyTimeTest()
        raw = self.getRawData(data[len(data) - 1])
        if raw == None:
            return 'no'
        soup = self.getSoup(raw)
        post_soup = self.get_post_soup(soup)

        self.commit_data(self.get_data_all(self.scrape_data(post_soup, data[len(data) - 1]), data[0], ','.join(data[1:-1])),batch_size=500)

# drivers = getWebDriver()

def main():
    blu = Products()
    blu.get_data_Textfile()


if __name__ == '__main__':
    main()