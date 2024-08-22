
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SNR.settings")
django.setup()

from userReviews.models import VendorReviews,VendorReviewsScore



import requests


class CalculateScores:

    def allreviewsLaptop(self):
        reviewData = VendorReviews.objects.filter(SNR_Category__icontains='Laptop')

        return reviewData


    def allreviews(self,query):
        reviewData = VendorReviews.objects.filter(SNR_Category__icontains=query)

        return reviewData

    def scoresLaptop(self):
        try:
            reviewData = CalculateScores().allreviewsLaptop();
            print reviewData.count()
            for data in reviewData:
                print data.SNR_Review
                print data.SNR_UPC
                # print str(reviewData[0].SNR_Review)

                headers = {'Content-Type': 'application/json'}
                userdata = {'category': "Laptop", 'review': str(data.SNR_Review)}
                try:
                    r = requests.post('http://ns519750.ip-158-69-23.net:8100/func/demo/', json=userdata,
                                      headers=headers)
                    # print('rrrr    ', r.content)
                    # print('rrrr    ', r)

                    review = VendorReviewsScore(reviews=data, SNR_VendorScoreAll=r.json())
                    review.save()

                except:
                    print "Error while calling...."




        except :
            print "Error in function"


    Categories = {
        "Laptop": "Laptops",
        # "Video": "Amazon_Instant_Videos",
        "Wearable": "Wearables",
        "Audio": "Musical_Instruments",
        "Cams": "Digital_Music",
        "Flowers": "Patio_Lawn_and_Gardens",
        "Cars": "Automotives",
        "Clothes": "Clothing_Shoes_and_Jewelry",
        "Jewelry": "Clothing_Shoes_and_Jewelry",
        "Books": "Books",
        # "Health": "Beauty_Products",
        "Office": "Office_Products",
        "games": "Video_Games",
        "Mobile": "Cell_Phones_and_Accessories",
        "Appliances": "Electronics",
        "Health": "Health_and_Personal_Care",
        "HomeGarden": "Home_and_Kitchen",
        "Sports": "Sports_and_Outdoors",
        "Smart home": "Tools_and_Home_Improvement",
        "Movies": "Movies_and_TV",
        "TV": "Movies_and_TV",
        "Toys": "Toys_and_Games"
    }


    def scoresCalc(self,shopCate, revCate ):
        try:
            print "Data: ",shopCate
            reviewData = CalculateScores().allreviews(shopCate);
            print "count: ",reviewData.count()
            for data in reviewData:
                print data.SNR_Review
                print data.SNR_UPC
                # print 'categories  ',Categories[cate]
                headers = {'Content-Type': 'application/json'}
                userdata = {'category': revCate, 'review': str(data.SNR_Review)}
            try:
                r = requests.post('https://www.reviewsai.com/func/demo/', json=userdata,
                                  headers=headers)
                # print('rrrr    ', r.content)
                # print('rrrr    ', r)

                review = VendorReviewsScore(reviews=data, SNR_VendorScoreAll=r.json())
                review.save()

            except:
                print "Error while calling...."

        except :
            print "Error in function"




    def startScoring(self):
        for key in self.Categories:
            print key, self.Categories[key]
            # self.allreviews(key)
            # reviewData = CalculateScores().allreviews(key);
            # print "count: ", reviewData.count()
            self.scoresCalc(key,self.Categories[key])

CalculateScores().scoresLaptop()
CalculateScores().startScoring()
