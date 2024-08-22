
import pandas
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import time
start_time = time.time()

import pickle

# pickle list object


list_pickle_path = './recommend_pickle.pkl'

# Create an variable to pickle and open it in write mode



def Calculating_Recommendation(dataset):
    # calculating tfidf vector to calculate the total frequency and to see which word is important for us
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    # getting matrix on the basis of title as it works on text
    tfidf_matrix = tf.fit_transform(dataset['title'])
    # calculating similarities between products by using cosing similarities with the help of dot product
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

    results = {}  # dictionary created to store the result in a dictionary format (ID : (Score,item_id))

    for idx, row in dataset.iterrows():  # iterates through all the rows
        # the below code 'similar_indice' stores similar ids based on cosine similarity. sorts them in ascending order. [:-5:-1] is then used so that the indices with most similarity are got. 0 means no similarity and 1 means perfect similarity
        similar_indices = cosine_similarities[idx].argsort()[
                          :-30:-1]  # stores 15 most similar items, you can change it as per your needs
        similar_items = [(cosine_similarities[idx][i], dataset['Product_id'][i]) for i in similar_indices]
        results[row['Product_id']] = similar_items[1:]
    return results
# below code 'function item(id)' returns a row matching the id along with Book Title. Initially it is a dataframe, then we convert it to a list


# the first argument in the below function to be passed is the id of the book, second argument is the number of books you want to be recommended


url = "output1.csv"


dataset = pandas.read_csv(url)

similarity_matrix=Calculating_Recommendation(dataset)
recommend_pickle = open(list_pickle_path, 'wb')
pickle.dump(similarity_matrix, recommend_pickle, protocol=2)
recommend_pickle.close()
