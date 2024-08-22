from contextlib import closing
from scrapetools import *
from django.db import connection
from products.models import AllProducts, Product_Review_AI



products_id_query = 'select {0} from products_product_reviews INNER JOIN products_allproducts'+\
                    ' ON products_product_reviews."Product_id"=products_allproducts.id {1};'

map = {
    'Cellphones & Accessories':"Cell_Phones_and_Accessories",
    "Electronics" : "Electronics",
    'Toys, kids & baby': "Toys_and_Games",
    'Office':"Office_Products",
    'Video games & consoles': "Video_Games",
    'Computer & Laptops' :"Laptops",
    "Sports" : "Sports_and_Outdoors",
    "Sporting Goods" : "Sports_and_Outdoors"
}



rev_format = {"category":"Toys_and_Games","review":"Nothing could be worst"}

with closing(connection.cursor()) as cursor:
    """
    cursor.execute(products_id_query.format('Distinct "SNR_Category"',""))
    cats = [i[0] for i in cursor.fetchall()]
    b=cats
    
    """

    for cat,map_cat in map.iteritems():
        rev_format["category"] = map_cat
        products_ids = []
        cursor.execute(products_id_query.format('Distinct "Product_id"',
                                                 'Where "SNR_Category" ILIKE \'%s\'' % cat
                                                 ))

        products_ids = [i[0] for i in cursor.fetchall()]
        for product_id in products_ids:
            cursor.execute(products_id_query.format('"SNR_Review_Title","SNR_Review_Body"',
                                                    'Where "Product_id"=%d ORDER BY "SNR_Review_UP" limit 30' % product_id
                                                    ))
            rev_data = cursor.fetchall()
            if rev_data:
                try:
                    rev_field = [u"{0}\n{1}".format(i[0],i[1])  for i in rev_data]
                except Exception as e:
                    pass
                rev_field = "\n\n".join(rev_field)
                rev_format["review"] = rev_field
                reviewai_response = getRawData("https://apis.reviewsai.com/func/demo/",data=rev_format,post=True,json=True)
                current_product = AllProducts.objects.get(pk=product_id)
                try:
                    rev_obj = Product_Review_AI.objects.create(
                                                Product=current_product,
                                                SNR_Review_Info=reviewai_response
                    )
                except Exception as e:
                    pass
            print ""