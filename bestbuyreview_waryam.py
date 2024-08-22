from scrapetools import *
from django.db import IntegrityError
from products.models import Product_Reviews, AllProducts


bestbuy_rev_api = "https://www.bestbuy.com/ugc/v2/reviews?sku=%s&page={0}"


def get_revs(sku):
    current_rev_api = bestbuy_rev_api % sku
    current_page = 1

    all_revs = []
    while True:

        current_rev_page = getRawData(current_rev_api.format(current_page),json=True)
        if current_rev_page["totalPages"] < current_page:
            break
        current_page+=1
        revs = current_rev_page["topics"]

        for current_rev in revs:
            current_review = {}
            try:
                current_review["SNR_Review_Title"] = parseHtml(current_rev["title"])
            except:
                pass

            try:
                current_review["SNR_Review_Author"] = current_rev["author"]
            except:
                pass

            try:
                current_review["SNR_Review_Body"] = parseHtml(current_rev["text"])
            except:
                pass

            try:
                current_review["SNR_Review_Stars"] = current_rev["rating"]
            except:
                pass


            try:
                current_review["SNR_Review_UP"]  = current_rev["positiveFeedbackCount"]
            except:
                pass

            try:
                current_review["SNR_Review_Down"] = current_rev["negativeFeedbackCount"]
            except:
                pass

            if current_review:
                all_revs.append(current_review)


    return all_revs



cr_bulk = lambda x,y: Product_Reviews.objects.bulk_create([Product_Reviews(Product=y,**i) for i in x])
def get_rev_table():
    all_rev_objects = AllProducts.objects.filter(SNR_Available__iexact="bestbuy")
    for current_item in all_rev_objects:
        print "Getting Reviews For Item ID: {0} from {1}".format(current_item.SNR_SKU,current_item.SNR_ProductURL)
        sku = current_item.SNR_SKU.split("BB",1)[-1]
        revs = get_revs(sku)
        print revs
        if revs:
            try:
                cr_bulk(revs,current_item)
            except IntegrityError:
                pass
            except:
                print "Some Database Error"



get_rev_table()