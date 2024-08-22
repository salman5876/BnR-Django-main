import sys, os
import traceback
from datetime import datetime

from django.db.models import Sum
from elasticsearch import NotFoundError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# PROJECT_ROOT = BASE_DIR.split('MudassirCode')[0]
# # PROJECT_ROOT PROJECT_ROOT= Path(__file__).parent.parent
# print('PROJECT_ROOT:  ',PROJECT_ROOT)
# sys.path.append(PROJECT_ROOT)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from django_elasticsearch_dsl import Document, fields, Index
from django_elasticsearch_dsl.registries import registry
from elasticsearch.helpers import parallel_bulk
from products.models import AllProducts
from categories.documents import AllProductsDocument
from elasticsearch_dsl import connections
from django.db.models import Q

def index_all_products(batch_size=300):
    try:
        # Create an Elasticsearch connection
        # connections.create_connection()

        # Check if the connection is established
        es = connections.get_connection()
        if es.ping():
            print('Elasticsearch connection successful')
        else:
            print('Elasticsearch connection failed')


        index_name = AllProductsDocument.Index.name
        index = Index(AllProductsDocument.Index.name)

        # Check if index already exist


        if not index.exists():
            index.create()
            print('Index created successfully')
        else:
            print('Index Already exists')

        # start_index = 847300
        # end_index = 907500

        start_index =28000
        end_index = 39000

        #  all_products = AllProducts.objects.all()
        # all_products = AllProducts.objects.using("newdb").exclude(
        #     SNR_Title__isnull=True,
        #     SNR_Title="00",
        #     SNR_Category__isnull=True,
        #     SNR_Category="00",
        #     SNR_ImageURL__isnull=True,
        #     SNR_ImageURL="00",
        #     SNR_isShow=True,
        #     SNR_Available = 'BEST BUY',
        #
        # ).order_by('id')[start_index:end_index]

        all_products = AllProducts.objects.using("newdb").exclude(
            Q(SNR_Title__isnull=True) |
            Q(SNR_Title="00") |
            Q(SNR_Category__isnull=True) |
            Q(SNR_Category="00") |
            Q(SNR_ImageURL__isnull=True) |
            Q(SNR_ImageURL="00") |
            Q(SNR_isShow=False) |
            Q(Q(SNR_Available='BestBuy') | Q(SNR_Available='BEST BUY'))
        ).order_by('id')[start_index:end_index]
        print('Prod Count: ', all_products.count())
        # 60533944

        actions = []
        for product in all_products:
            # try:
            #     document = AllProductsDocument.get(product.id)
            # except:
            #     document = None

            # document = None
            # try:
            #     document = AllProductsDocument.get(id=product.id)
            # except NotFoundError:
            #     pass

            # Check if the document exists
            try:
                document = AllProductsDocument.exists(id=product.id)
            except NotFoundError:
                document = False

            if not document:
                try:
                    action = {
                        '_op_type': 'index',
                        '_index': index._name,
                        '_id': product.id,
                        '_source': {
                            # Map fields to source data
                            'SNR_SKU': product.SNR_SKU,
                            'SNR_Title': product.SNR_Title,
                            'SNR_ModelNo': product.SNR_ModelNo,
                            'SNR_Brand': product.SNR_Brand,
                            'SNR_UPC': product.SNR_UPC,
                            'SNR_Available': product.SNR_Available,
                            'SNR_ProductURL': product.SNR_ProductURL,
                            'SNR_ImageURL': product.SNR_ImageURL,
                            'SNR_Description': product.SNR_Description,
                            'SNR_Description_Mobile': product.SNR_Description_Mobile,
                            'SNR_isShow': product.SNR_isShow,
                            'SNR_Date': product.SNR_Date,
                            'SNR_Category': product.SNR_Category,
                            'SNR_Condition': product.SNR_Condition,
                            'SNR_PriceBefore': product.SNR_PriceBefore,
                            'SNR_CustomerReviews': product.SNR_CustomerReviews,
                            'SNR_Price': product.SNR_Price,
                            'SNR_SubCategory': product.SNR_SubCategory,

                        }
                    }
                    actions.append(action)
                except Exception as e:
                    print(e)

                # if len(actions) == batch_size:
                # if len(actions) == 5:
                #     # success, _ = parallel_bulk(index._get_connection(), actions, thread_count=4, chunk_size=batch_size)
                #     success = parallel_bulk(index._get_connection(), actions, thread_count=4, chunk_size=batch_size)
                #     print(f'Indexed {success} is successfully documents')
                #     actions = []



                if len(actions) == batch_size:
                    # print(actions)
                    success = parallel_bulk(index._get_connection(), actions, thread_count=4, chunk_size=batch_size)

                    # Iterate over the results
                    for result in success:
                        if not result[0]:
                            # Loop ( error_handling -->>  )
                            print(f"Error indexing document: {result[1]['index']['_id']}")

                    print(f'Indexed {len(actions)} documents successfully')
                    actions = []
            else:
                print('Already indexed')
        # print(actions)

        if actions:
            # success, _ = parallel_bulk(index._get_connection(), actions, thread_count=4, chunk_size=batch_size)
            success = parallel_bulk(index._get_connection(), actions, thread_count=4, chunk_size=batch_size)
            # Iterate over the results
            for result in success:
                if not result[0]:
                    # Handle indexing failures or errors
                    print(f"Error indexing document: {result[1]['index']['_id']}")

            print(f'Indexed {len(actions)} documents successfully')
            # print(f'Indexed {success}  is successfully documented')


    except Exception as e:
        print(e)

def delete_all_products():
    index_name = AllProductsDocument.Index.name
    index = Index(AllProductsDocument.Index.name)

    # Check if index alr%eady exists
    if not index.exists():
        print("Index already exists")
    else:
        index.delete()

from elasticsearch import Elasticsearch
def ilm_policy():
    from elasticsearch import Elasticsearch

    # Replace with the appropriate Elasticsearch URL
    es = Elasticsearch(["http://localhost:9200"])

    index_name = "all_product_index"

    try:
        ilm_explain = es.ilm.explain(index=index_name)
        if "index" in ilm_explain and "managed" in ilm_explain["index"]:
            if ilm_explain["index"]["managed"]:
                print(f"Index {index_name} is managed by ILM.")
            else:
                print(f"Index {index_name} is not managed by ILM.")
        else:
            print(f"Index {index_name} does not have ILM information.")
    except Exception as e:
        print(f"Error: {e}")


index_all_products()
# delete_all_products()