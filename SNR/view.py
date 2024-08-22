# from src import sell4bids
from rest_framework.decorators import api_view

# from . import data_cleaning
# import recommend_content as rc
import pickle
import json
import ast
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST','GET'])
def review_testing(request):
    if request.method == 'GET':
        dict={
            "Title": "Testing"
        }
        return Response(dict, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = request.data
        res = []
        for key,value in data.items():
            res.append(key)

            value = str(value)
            print('Value iss', value)

            # print(value[11:-2])
            res.append(value[12:-2])


        return Response(res, status=status.HTTP_201_CREATED)



@api_view(['POST'])
def review_Recommendation(request):
    if request.method=='POST':
        print("in if")
        total_recommendations=set()
        recommendation_per_item=set()
        list_pickle_path = './SNR/recommend_pickle.pkl'
    # print("req:",request)
    # request=json.loads(open(request).read())
        pickle_in = open(list_pickle_path, "rb")
        similarity_matrix = pickle.load(pickle_in)

        print("title")
        print(request)

        json_object = request.data

        print(json_object)
        for key,value in json_object.items():


            # value = value.replace("'","/")
            for key1,value1 in value.items():
                if key1=='title':
                    title1=value1



                    recommendation_per_item=rc.recommend(title1,25,similarity_matrix)
                    print(recommendation_per_item)
            total_recommendations=total_recommendations.union(recommendation_per_item)
            print(total_recommendations)
    total_recommendations=list(total_recommendations)
    # total_recommendations=json.dumps(total_recommendations)
    return Response(total_recommendations, status=status.HTTP_202_ACCEPTED)


