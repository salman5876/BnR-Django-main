import pickle
import pandas




def search_item_title(title):
    return dataset.loc[dataset['title'] == title]['title'].tolist()[0]
def search_item_product_id(id):
    return dataset.loc[dataset['Product_id'] == id]['Product_id'].tolist()[0]
def GetFullRecord(id):
    return dataset[dataset.Product_id==id]
def getCategory(id):
    return dataset.loc[dataset['title'] == id]['Category'].tolist()[0]

def recommend(id, num,similarity_matrix):

    state = set(dataset['State'][dataset.title == id])
    title=id
    id=set(dataset['Product_id'][dataset.title==id])

    category=set(dataset['Category'][dataset.title==title])


    # print("category:", category)

    list_of_elements = set()

    if (not state or not category):
        return list_of_elements

    state=next(iter(state))
    category=next(iter(category))
    # print("category:",category)



    id=next(iter(id))


    check=0
    print("num=",num)
    recs = similarity_matrix[id][:num]
    count=1
    for rec in recs:
        other_state=set(dataset['State'][dataset.Product_id==rec[1]])
        other_state=next(iter(other_state))
        other_category=set(dataset['Category'][dataset.Product_id==rec[1]])
        other_category=next(iter(other_category))
        # print("other_category:",other_category)

        # print(other_state)
        # print("You may also like to buy: " + search_item_product_id(rec[1]) + " (score:" + str(rec[0]) + ")" + "category:",other_category)
        if(other_state==state and rec[0] > 0 ):

            print("You may also like to buy: " + search_item_product_id(rec[1]) + " (score:" + str(rec[0]) + ")")
            list_of_elements.add(search_item_product_id(rec[1]))

            check=1
        # print(count)
        count += 1


    return list_of_elements
# with open('./output.csv', 'r') as f:
#     dataset = pandas.read_csv(f)

url = './SNR/output1.csv'

list_pickle_path = './SNR/recommend_pickle.pkl'
dataset = pandas.read_csv(url)



# pickle_in = open(list_pickle_path,"rb")
# similarity_matrix = pickle.load(pickle_in)
#
# items=recommend('White Macbook', 25,similarity_matrix)
# print(items)