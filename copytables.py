import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()
from multiprocessing.dummy import Pool as ThreadPool
import os
from os import listdir

from laptop.models import Laptop_DB
from wearables.models import Wearable_DB
from mobile.models import Mobile_DB
from products.models import TV, Cams, CarsElectronics, VideoGames, Toys, SmartHomes, Audio, \
    Books, ComputerSoftware, Applinces, Movies, OfficeSupply, HealthandFitness, ElectronicGadgets, SportingGoods, \
    Furniture, Jewelry, HomeandGarden, FlowerandPlants, \
    Clothing, Arts, AllProducts
from products.serializers import AllProducts_Serializer
import multiprocessing


print multiprocessing.cpu_count()

# directoryPath=scrapingScripts
# files = listdir(directoryPath)

files=[Laptop_DB,Books,Clothing,Arts,ComputerSoftware,Movies,OfficeSupply,Furniture,HomeandGarden,FlowerandPlants,Jewelry,HealthandFitness,ElectronicGadgets,SportingGoods, Applinces,Wearable_DB, Mobile_DB,TV,Cams,CarsElectronics,Audio,Toys ,VideoGames,SmartHomes]


def run(file):
    request={}
    print(file)
    data = file.objects.all()
    for item in data:

        request["SNR_Price"] = item.SNR_Price
        request["SNR_Brand"] = item.SNR_Brand
        request["SNR_Available"] = item.SNR_Available
        request["SNR_Description"] = item.SNR_Description
        request["SNR_Title"] = item.SNR_Title
        request["SNR_ProductURL"] = item.SNR_ProductURL
        request["SNR_ModelNo"] = item.SNR_ModelNo
        request["SNR_SKU"] = item.SNR_SKU
        request["SNR_UPC"] = item.SNR_UPC
        request["SNR_Category"] = "Laptop"
        request["SNR_ImageURL"] = item.SNR_ImageURL
        request["SNR_CustomerReviews"] = item.SNR_CustomerReviews

        serializer1 = AllProducts_Serializer(data=request)
        try:
            if serializer1.is_valid():
                print("---")

                serializer1.save()
            else:
                print("bad json")
        except:
            continue



pool = ThreadPool(multiprocessing.cpu_count()*4)

results = pool.map(run, files)

pool.close()
pool.join()
