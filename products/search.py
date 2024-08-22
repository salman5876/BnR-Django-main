from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch_dsl.connections import connections
import datetime

connections.create_connection(hosts=['ns3031341.ip-149-202-94.eu:9200'])


class SNRIndex(DocType):
    SNR_SKU = Text()
    SNR_Title = Text()
    SNR_ModelNo = Text()
    SNR_Brand = Text()
    SNR_UPC = Text()
    SNR_Category = Text()
    SNR_Price = Text()
    SNR_CustomerReviews= Text()

    SNR_Available = Text()
    SNR_ProductURL = Text()
    SNR_ImageURL = Text()
    SNR_Description = Text()
    SNR_isShow = Text()


    SNR_Date = Date()

    class Meta:
        index = 'snr-index'


def bulk_indexing():
    from products.models import AllProducts
    SNRIndex.init(index='snr-index')
    es = Elasticsearch(hosts=['ns3031341.ip-149-202-94.eu:9200'])

    es.indices.delete(index='snr-index', ignore=[400, 404])
    print ('deleteeeee')
    bulk(client=es, actions=(b.indexing() for b in AllProducts.objects.all().iterator()))


