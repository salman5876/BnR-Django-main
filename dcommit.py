import json
import binascii
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from products.serializers import AllProducts_Serializer
from products.models import AllProducts

import sys

request = binascii.unhexlify(sys.argv[1]).decode('utf8')

request = json.loads(request)


try:
    serializer = AllProducts_Serializer(data=request)

    if serializer.is_valid():
        print("---")
        serializer.save()
    else:
        print "bad json"
        print serializer.errors

except Exception as e:
    try:
        with open("exceptions.txt", "a") as w:
            w.write(str(e) + " " + json.dumps(request) + "\n")
    except:
        pass