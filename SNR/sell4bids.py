import pandas as pd
import json
import csv

sell=pd.read_json('./sell4bids-4affe-products-export.json')
print(sell)


def read_json(filename):
    return json.loads(open(filename).read())

import json





json=read_json('./sell4bids-4affe-products-export.json')



sell4bids = pd.DataFrame(columns=['Category','Auction_type','State','Product_id','title','uid'])

# i=1
print(len(json))











title1=""
uid=""

#for count in range(0,10):
total_products=0
i=0
for categories in json.keys():
    x = json[categories]
    # print("category:",x)
    #sell4bids.loc[i,'Category'] = categories
    types = x.keys()

    for type in x.keys():
        states = x[type]
        # print("Auction_type", type)
        products = len(states.keys())
        total_products+=products
        for state in states.keys():
            # print("state:",state)
            products=states[state]
            for product in products.keys():
                # print("product:",product)
                product_data=products[product]
                for data in product_data.keys():
                    if data=='title':
                        # print("title:",product_data[data])
                        title1=product_data[data]
                        # print(title1)
                    if data=='uid':
                        # print("uid:",product_data[data])
                        uid=product_data[data]

                sell4bids.loc[i,'Category']=categories

                sell4bids.loc[i, 'Auction_type'] = type
                sell4bids.loc[i, 'State']=state
                sell4bids.loc[i,'Product_id']=product
                sell4bids.loc[i, 'title']=title1
                sell4bids.loc[i, 'uid']=uid
                print(sell4bids)
                i=i+1



print('Category: ', categories, 'No of Products: ', len(x.keys()))

print('Total Products ------------------------> : ', total_products)

# print(sell4bids)
print(sell4bids)
sell4bids.to_csv('./output.csv',index=False)


