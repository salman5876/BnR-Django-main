
# URLS
url(r'^filterappliencesall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLAppliences, name="Filter"),
url(r'^filtertvsall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLTV, name="Filter"),
url(r'^filtergadgetssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLGadgets, name="Filter"),
url(r'^filtercamssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterCams, name="Filter"),
url(r'^filtercarselecsall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLCarsElec, name="Filter"),

url(r'^filtergamessall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLVideo, name="Filter"),

url(r'^filtertoyssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLToys, name="Filter"),
url(r'^filtersmarthomesall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSmartHome, name="Filter"),
url(r'^filteraudiosall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLAudio, name="Filter"),
url(r'^filtersoftwaresall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSoftware, name="Filter"),
url(r'^filtermoviessall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLMovies, name="Filter"),
url(r'^filterbookssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLBooks, name="Filter"),
url(r'^filterfurnituresall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLFurniture, name="Filter"),
url(r'^filterflowerssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLFlower, name="Filter"),
url(r'^filterclothessall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLClothes, name="Filter"),
url(r'^filterartssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLArts, name="Filter"),
url(r'^filterjewelrysall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLJewelry, name="Filter"),
url(r'^filterhomegardensall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLHomeGarden, name="Filter"),
url(r'^filtersportssall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSports, name="Filter"),
url(r'^filterofficesupplysall/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLOffice, name="Filter"),


# URLS
url(r'^filterappliencesallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLAppliencesASC, name="Filter"),
url(r'^filtertvsallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLTVASC, name="Filter"),
url(r'^filtergadgetssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLGadgetsASC, name="Filter"),
url(r'^filtercamssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterCamsASC, name="Filter"),
url(r'^filtercarselecsallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLCarsElecASC, name="Filter"),

url(r'^filtergamessallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLVideoASC, name="Filter"),

url(r'^filtertoyssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLToysASC, name="Filter"),
url(r'^filtersmarthomesallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSmartHomeASC, name="Filter"),
url(r'^filteraudiosallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLAudioASC, name="Filter"),
url(r'^filtersoftwaresallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSoftwareASC, name="Filter"),
url(r'^filtermoviessallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLMoviesASC, name="Filter"),
url(r'^filterbookssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLBooksASC, name="Filter"),
url(r'^filterfurnituresallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLFurnitureASC, name="Filter"),
url(r'^filterflowerssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLFlowerASC, name="Filter"),
url(r'^filterclothessallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLClothesASC, name="Filter"),
url(r'^filterartssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLArtsASC, name="Filter"),
url(r'^filterjewelrysallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLJewelryASC, name="Filter"),
url(r'^filterhomegardensallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLHomeGardenASC, name="Filter"),
url(r'^filtersportssallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSportsASC, name="Filter"),
url(r'^filterofficesupplysallASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLOfficeASC, name="Filter"),


# URLS
url(r'^filterappliencesallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLAppliencesDESC, name="Filter"),
url(r'^filtertvsallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLTVDESC, name="Filter"),
url(r'^filtergadgetssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLGadgetsDESC, name="Filter"),
url(r'^filtercamssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterCamsDESC, name="Filter"),
url(r'^filtercarselecsallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLCarsElecDESC, name="Filter"),

url(r'^filtergamessallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLVideoDESC, name="Filter"),

url(r'^filtertoyssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLToysDESC, name="Filter"),
url(r'^filtersmarthomesallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSmartHomeDESC, name="Filter"),
url(r'^filteraudiosallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLAudioDESC, name="Filter"),
url(r'^filtersoftwaresallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSoftwareDESC, name="Filter"),
url(r'^filtermoviessallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLMoviesDESC, name="Filter"),
url(r'^filterbookssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLBooksDESC, name="Filter"),
url(r'^filterfurnituresallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLFurnitureDESC, name="Filter"),
url(r'^filterflowerssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLFlowerDESC, name="Filter"),
url(r'^filterclothessallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLClothesDESC, name="Filter"),
url(r'^filterartssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLArtsDESC, name="Filter"),
url(r'^filterjewelrysallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLJewelryDESC, name="Filter"),
url(r'^filterhomegardensallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLHomeGardenDESC, name="Filter"),
url(r'^filtersportssallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLSportsDESC, name="Filter"),
url(r'^filterofficesupplysallDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$', views.FilterALLOfficeDESC, name="Filter"),
