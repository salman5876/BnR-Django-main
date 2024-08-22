import bottlenose
import json
import xmltodict
query = 'iphone'

amazon = bottlenose.Amazon('AKIAJYH5LPTVAMBU6NOQ', 'DfGaLxsy9ftS/672f0VxCWgoXecj3LRxNoqLMNPA','mobilea0fe6ba-20')
response = amazon.ItemSearch(Keywords=query, SearchIndex="All",ResponseGroup='ItemAttributes,Images,Large', limit=100, )

response = json.dumps(xmltodict.parse(response), indent=4)
response = json.loads(response)
items = []
print response['ItemLookupResponse']['Items']['Item']
