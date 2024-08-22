from scrapetools import *

import re

start_url = "https://www.amazon.com/gp/goldbox"



def get_short_url(urlData):
    try:
        urlData = urlData[urlData.index("<script>"):urlData.rindex("</script>")]
    except:
        pass

    return urlData

def getDeals(urlData=False):
    if not urlData:
        urlData = getRawData(start_url)

    urlData = get_short_url(urlData)



    data = re.finditer('"sortedDealIDs"\s*:\s*\[',urlData)

    string_pat = next(re.finditer('"resources"\s*:\s*{',urlData)).regs[0][1]-1


    dealsIds = []
    strings_data = getJsonData(urlData[string_pat:],"{","}")
    market_id = next(re.finditer('"marketplaceId"\s*:\s*"(\w+)",',urlData)).group(1)
    while True:
        try:

            temp = next(data)


            endindex = temp.regs[0][1]-1
            dealsIds.extend(getJsonData(urlData[endindex:]))
            break
        except StopIteration:
            pass

    import subprocess

    cprocess = """curl 'https://www.amazon.com/xa/dealcontent/v2/GetDeals' --data '{"requestMetadata":{"marketplaceID":"%s","clientID":"goldbox_mobile_pc"},"dealTargets":%s,"responseSize":"ALL","widgetContext":{"pageType":"GoldBox","subPageType":"main","deviceType":"pc"}}' --compressed"""

    all_deals = []
    while dealsIds:
        dtemp = json.dumps([{"dealID": i} for i in dealsIds[:100]])
        dealsIds = dealsIds[100:]
        temp = cprocess % (market_id, dtemp)
        p = subprocess.Popen(temp, stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        output, err = p.communicate()

        output = json.loads(output)
        all_deals.append(output)

    for i in all_deals:
        deal_details =i["dealDetails"]

        for deal_id, deal_data in deal_details.iteritems():

            try:

                bamount = -1.0
                try:
                    bamount = deal_data["minBAmount"]
                except:
                    pass

                temp_id = deal_data['impressionAsin'].encode("utf-8")
                temp_url = "https://www.amazon.com/dp/{0}".format(temp_id)
                temp_after = deal_data['minCurrentPrice']

                if temp_after==bamount:
                    bamount = -1.0


                temp = {
                    "SNR_SKU": "AZ"+temp_id,
                    "SNR_Title": deal_data['title'].encode("utf-8"),
                    "SNR_ProductURL": temp_url,
                    "SNR_ImageURL": deal_data["primaryImage"].encode("utf-8"),
                    "SNR_Category": "Not Available".encode("utf-8"),
                    "SNR_PriceBefore": bamount,
                    "SNR_PriceAfter": temp_after,
                    "SNR_Available": "Amazon".encode("utf-8")
                }
                yield temp

            except:
                pass


getDeals()