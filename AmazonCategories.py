from AmazonScrapeTools import ScrapeTools
import re
from itertools import imap

class Categories(ScrapeTools):
    start_url = 'https://www.amazon.com/gp/site-directory'
    # instance attributes
    def __init__(self):
        super(Categories,self).__init__(poolno=1)
    #     self.proxy = proxy
    #     self.driver = driver

    # instance method
    # def sing(self, song):
    #     return "{} sings {}".format(self.proxy, song)
    #
    # def dance(self):
    #     return "{} is now dancing".format(self.driver)

    def appendLog(self,data):  #############  Appending URLs in File #############
        try:
            with open("AmazonAutomotive.txt", "a") as w:
                w.write(data + "\n")
                print data
        except Exception as e:
            pass


    def get_cats(self):  ################### Getting All Category and SubCategory Links ############################
        # ProxyTimeTest()
        # self.driver.get(self.start_url)

        raw = self.getRawData(self.start_url)
        if "did not match any products" in raw:
            return []
        soup = self.getSoup(raw)
        cat_soup = soup.select("div.fsdContainerWrapper div.fsdColumn div.fsdDeptBox")
        all_data = []
        for i in cat_soup:

            cat_label = i.select_one("h2.fsdDeptTitle").text.strip().capitalize()
            print cat_label
            if cat_label == 'Movies, music & games':
                print 'INNNNNNNNNNNNn'
                links_div = i.select("div.fsdDeptCol a.fsdDeptLink")

                for link in links_div:
                    current_label = link.text.encode('utf-8').strip().capitalize()
                    print 'Subbbbbb', current_label

                    current_link = self.getAbsUrl(self.start_url, link["href"])
                    all_data.append((cat_label, current_label, current_link))

        return all_data

    def extract_data(self,elem):  ########### Requesting each Category URL #################
        all_visited = set()
        cat_label, subcat_label, cat_url = elem
        current_urls = [{"url": cat_url, "cat": cat_label}]

        while current_urls:
            temp = current_urls.pop()
            url_temp = temp["url"]
            if "/samples/" in url_temp:
                continue

            if "redirect.html" in url_temp:
                continue

            if url_temp not in all_visited:
                cat_temp = temp["cat"]
                n = True
                count = 0

                while n:
                    n = False
                    try:
                        # ProxyTimeTest()
                        # driver.get(url_temp)
                        raw = self.getRawData(url_temp)
                        if "did not match any products" in raw:
                            break
                        current_soup = self.getSoup(raw)
                    except Exception as e:
                        if count < 3:
                            n = True
                            count += 1

                    self.SubCat(current_soup, url_temp, subcat_label)

    def get_data(self):  ############ Main Function to get Category URLs and then extracting URLs one by one ##################
        cats_data = [i for i in self.get_cats()]
        print cats_data

        def serial():
            for i in imap(self.extract_data, cats_data):
                pass

        serial()

    def getSub_Cat(self,url, cat):  ######## Sub Function to get SubCat URLs ################
        all_data1 = []
        all_data2 = []
        # ProxyTimeTest()
        # driver.get(url)
        url1 = self.getRawData(url)
        # proxy = url1[1]
        soup1 = self.getSoup(url1)
        data_soup1 = soup1.select_one("div[aria-label*=Categories] div#leftNav")
        if data_soup1:
            try:
                data_soup1 = soup1.select("ul.s-ref-indent-one")
                data_soup1 = data_soup1[1].select("div[aria-live=polite] li span.a-list-item a")
            except:
                data_soup1 = soup1.select("ul.s-ref-indent-two")
                data_soup1 = data_soup1[0].select("div[aria-live=polite] li span.a-list-item a")

        if data_soup1:
            for i in data_soup1:
                cl1 = i.text.strip().capitalize()
                all_data1.append({"url": self.getAbsUrl(url, i["href"]), "Cat": cat, "SubCat": cl1})

            if all_data1:
                for k in all_data1:
                    # ProxyTimeTest()
                    # driver.get(k['url'])
                    url2 = self.getRawData(k['url'])
                    # proxy = url2[1]
                    soup2 = self.getSoup(url2)
                    data_soup2 = soup2.select_one("div[aria-label*=Categories] div#leftNav")
                    try:
                        data_soup2 = soup2.select("ul.s-ref-indent-one")
                        data_soup2 = data_soup2[2].select("div[aria-live=polite] li span.a-list-item a")
                        for l in data_soup2:
                            cl2 = l.text.strip().capitalize()
                            all_data2.append({"url": self.getAbsUrl(k['url'], l["href"]), "Cat": k['Cat'], "SubCat": cl2})

                        # print all_data1
                        all_data1.remove(k)
                    except:
                        pass

                for m in all_data2:
                    all_data1.append(m)

            return all_data1

    def SubCat(self,soup, url, subcat):  ############## Getting All URLs for every Category. ##################
        subcat = re.sub(',', '', subcat)
        if subcat != 'Luxury beauty' or subcat != 'All beauty':
            all_data = []
            all_data1 = []
            cat = ''
            all_data2 = []
            try:
                data_soup = soup.select_one("div.browseBox")
                cat = data_soup.select_one("h3").text.strip()
                data_soup = data_soup.select("ul li a")
            except:
                data_soup = soup.select_one("div[aria-label*=Categories] div#leftNav")
                if data_soup:
                    data_soup = soup.select("ul[class*=-indent-] div[aria-live=polite] li span.a-list-item a")

            if data_soup:
                for i in data_soup:
                    cl = i.text.strip().capitalize()
                    all_data.append({"url": self.getAbsUrl(url, i["href"]), "cat": cl})
                if all_data:
                    for j in all_data:
                        # print j
                        # try:
                        #     all_data1 = [i for i in self.getSub_Cat(j['url'], j['cat'])]
                        #     for data in all_data1:
                        #         all_data2.append(data)
                        # except:
                        all_data1 = {'SubCat': j['cat'], 'url': j['url']}
                        all_data2.append(all_data1)

                    if all_data1:
                        print all_data2
                        for k in all_data2:
                            k['SubCat'] = re.sub(',', '', k['SubCat'])
                            self.appendLog(','.join((subcat,k['SubCat'],k['url'])).encode('utf-8').strip())
                        # appendLog(str(j['url']))
                    # raw = getRawData(j['url'], proxy=proxy)






def main():
    blu = Categories()
    blu.get_data()


if __name__ == '__main__':
    main()