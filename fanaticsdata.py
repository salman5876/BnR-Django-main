from scrapetools import *

start_url = 'https://www.fanatics.com/'

def get_cats():
    soup = False
    while not soup:
        soup = getSoup(url=start_url).find(
            "nav",class_="top-nav-container")

    links = [(i.text.strip(),getAbsUrl(start_url,i["href"])) for i in soup.select("a[id*=top-nav/]") if not i["href"].startswith("#")]
    links.extend(
        [(i.text.strip(),getAbsUrl(start_url,i["href"])) for i in soup.select_one("a#top-nav/12").select("a.top-nav-link") if not i["href"].startswith("#")])

    return links

def is_posts(soup):
    return soup.select_one("div.product-grid-container")


def get_subcats(soup,url):
    try:
        team_soup = soup.select_one("div.team-list-content").select('a.team-list-link')
        return [(i.text.strip(),getAbsUrl(url,i["href"])) for i in team_soup]
    except:
        pass


def scrape_data(soup,ur):
    is_next = True
    and_url = "&pageNumber={0}"
    t_url = ur+and_url
    current_page = 1
    while is_next:
        is_next = False

        all_items = soup.select("div.product-card")

        for current_item in all_items:
            try:
                price_div = current_item.select_one("div[data-talos=srpProductPrice]")
                image_div = current_item.select_one("div.product-image-container a[data-trk-id]")
                request = {}
                price = float(price_div.select_one("div.regular-price").text.strip().replace(
                    "$","").replace(",",""))

                try:
                    price_before = float(price_div.select_one("div.sale-price").text.strip().replace(
                        "$","").replace(",",""))
                except:
                    price_before = -1.0

                request["SNR_ModelNo"] = "00"
                request["SNR_UPC"] = "00"
                request["SNR_Available"] = "Fanatics"
                request["SNR_Description"] = "Visit site to see description"
                request["SNR_SKU"] = "FN" +image_div["data-trk-id"][2:]
                request["SNR_Category"] = "Sports Apparel"

                request["SNR_Condition"] = "00"
                request["SNR_PriceBefore"] = price_before
                request["SNR_Price"] = price
                request["SNR_CustomerReviews"] = 0.0
                request["SNR_ProductURL"] = getAbsUrl(ur,image_div["href"])
                image_div = image_div.img
                request["SNR_Title"] = image_div["alt"]
                image = image_div["src"]
                if image.startswith("//"):
                    image = "https:"+image

                request["SNR_ImageURL"] = image

                yield request
            except:
                pass


        try:
            next_div = soup.select("li.next-page")[0]["class"]
            if "disabled" not in next_div:
                current_page+=1
                is_next = True
                ur = t_url.format(current_page)
                soup = False
                while not soup:
                    soup = is_posts(getSoup(url=ur))

        except:
            pass

def get_data():
    cats = get_cats()

    while cats:
        current_cat, current_url = cats.pop()
        try:
            temp = current_url.rindex("?")
            current_url = current_url[:temp]
        except:
            pass

        current_url +="?pageSize=96&sortOption=TopSellers"
        temp = False
        total_timeout = 10
        tmap = {}
        while not temp:
            try:
                tmap[current_url]+=1
            except:
                tmap[current_url] = 1

            if tmap[current_url]>=5:
                break

            current_raw = getRawData(current_url)
            current_soup = getSoup(current_raw)
            posts_soup = is_posts(current_soup)

            if posts_soup:
                temp = scrape_data(posts_soup,current_url)
                for i in temp:
                    i["SNR_Brand"] = i["SNR_SubCategory"] = current_cat
                    yield i
            else:
                temp = get_subcats(current_soup,current_url)
                if temp:
                    cats.extend(temp)


commit_data(get_data())