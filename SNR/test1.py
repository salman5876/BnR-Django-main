import pandas as pd
import json
import csv
import pickle

from src import recommend_content as rc
def read_json(filename):
    return json.loads(open(filename).read())


json=read_json('./products.json')

sell4bids = pd.DataFrame(columns=['product_id','title'])
list_pickle_path = './recommend_pickle.pkl'
pickle_in = open(list_pickle_path, "rb")
similarity_matrix = pickle.load(pickle_in)
print(len(json))

for key,value in json.items():
    print(key,value)


for key, value in json.items():
        # value = value.replace("'","/")

    value = str(value)
    title1 = value[11:-2]
    print("title1", title1)
print(rc.recommend(title1,10,similarity_matrix))


