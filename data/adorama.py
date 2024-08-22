import socket

import socks
from scrapetools import *
import scrapy

ip='127.0.0.1' # change your proxy's ip
port = 9150 # change your proxy's port
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, ip, port)
socket.socket = socks.socksocket

ad_url = "https://www.adorama.com/specials/l/?Page={0}"
headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

class AdoramaDeals:
    name = "adoramadeals"
    def start_requests(self):
        ur = ad_url.format(1)
        self.get_deals(getRawData(url=ur,retry_code=[403]),ur)


    def get_deals(self,response,ur):
        response = BeautifulSoup(response,"lxml")
        all_items_data = response.select("div[data-sku]")


        for current_item in all_items_data:
            try:
                item_id = current_item["data-sku"]
                item_id = "AD" + item_id
                image_div = current_item.select_one("div.item-img a")

                item_url = image_div["href"]
                item_url = getAbsUrl(ur,item_url)

                image_div = image_div.select_one("img.productImage")

                try:
                    image = image_div["data-src"]
                except:
                    image = image_div["src"]

                item_image = getAbsUrl(ur,image)

                item_title = current_item.select_one("div.item-details h2[itemprop=name] a").text.strip()

                price_div = current_item.select_one("div.item-actions div.prices")
                before_div = str(price_div.select_one("p[class*=breakdown] s.price-reg-has-sibs"))
                try:
                    before_price = float( patSearch("\$([\d,\.]+)",before_div).group(1).replace(",","")  )
                except:
                    before_price = -1.0

                before_div = str(price_div.select_one("strong.your-price"))
                price = float( patSearch("\$([\d,\.]+)",before_div).group(1).replace(",","")  )

                current_item = {
                    "SNR_SKU": item_id,
                    "SNR_Title": item_title,
                    "SNR_ProductURL": item_url,
                    "SNR_ImageURL": item_image,
                    "SNR_Category": "Not Available",
                    "SNR_PriceBefore": before_price,
                    "SNR_PriceAfter": price,
                    "SNR_Available": "Adorama"
                }

                commitdeal(current_item)



            except Exception as e:
                pass


        try:
            ur = response.select_one("a.page-next")["href"]

            if ur:
                self.get_deals(getRawData(url=ur,retry_code=[403]), ur)
        except:
            pass

AdoramaDeals()