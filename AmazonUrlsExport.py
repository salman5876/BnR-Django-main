import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AmazonURLs_Serializer

lst = ['AmazonMovie.txt']
for i in lst:
    with open(i, 'r') as f:
        data = [i.split(',') for i in f]
        for index, j in enumerate(data):
            j[len(j) - 1] = j[len(j) - 1][:-1]

        for item in data:
            item1={'Cat':item[0].decode('utf-8'),'SubCat':item[1].decode('utf-8'),'url':item[2].decode('utf-8')}
            serializer = AmazonURLs_Serializer(data=item1)

            if serializer.is_valid():
                print("INSERT")
                serializer.save()
            else:
                print 'Error'