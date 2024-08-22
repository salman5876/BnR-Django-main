from django.urls import re_path as url

from . import APIS

urlpatterns = [

    url(r'^suggestions/(?P<query>.+)/$', APIS.AutoComplete, name="Search Result"),
    url(r'^suggestions1/(?P<query>.+)/$', APIS.AutoComplete1, name="Search Result"),

    url(r'^filterbyprice/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/$', APIS.FilterProductsbyprice,
        name="Search Result"),
    url(r'^filterbypriceASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/$', APIS.FilterProductsbypriceASC,
        name="Search Result"),
    url(r'^filterbypriceDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/$', APIS.FilterProductsbypriceDESC,
        name="Search Result"),

    url(r'^QueryCategories$', APIS.getAll_CatsQueries, name=""),

    url(r'^filterbycategory/$', APIS.FilterProductsbyCat, name="Search Result"),
    #
    # url(r'^filterbyurl/(?P<query>.+)/$', APIS.FilterbyURL, name="Search Result"),
    # url(r'^filterbyurlASC/(?P<query>.+)/$', APIS.FilterbyURLASC, name="Search Result"),
    # url(r'^filterbyurlDESC/(?P<query>.+)/$', APIS.FilterbyURLDESC, name="Search Result"),

    # url(r'^CountallproductsBrandMerchants/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/$',APIS.CountBrandMerchantsAllProducts, name="Search Result"),

    url(
        r'^CountallproductsBrandMerchants/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.CountBrandMerchantsAllProducts_Search, name="Search Result"),

    url(
        r'^findsearchedproducts_ebay/(?P<query>.+)/$',
        APIS.findproductsfromebay, name="Search Result"),

    url(
        r'^filterReviewebay/(?P<query>.+)/$',
        APIS.FilterProductsRevsebay, name="Search Result"),

   url(
        r'^findsearchedproducts_amazon/(?P<query>.+)/$',
        APIS.findproductsfromamazon, name="Search Result"),


    url(
        r'^insertsearchedproducts_ebay/(?P<query>.+)/$',
        APIS.insertproductsfromebay, name="Search Result"),

    url(
        r'^findTitlefromUPC/(?P<upc>.+)/$',
        APIS.findtitlefromUPC, name="Search Result"),
    url(
        r'^findcredential/$',
        APIS.findcredential, name="Search Result"),
    # url(r'^filterallproductsWITHOUTLIKE/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$', APIS.FilterAllProducts_Search_Similar, name="Search Result"),
    url(
        r'^filterallproductsDateDSC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search, name="Search Result"),

    # url(
    #     r'^filterallproductsASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
    #     APIS.FilterAllProductsASC_Search, name="Search Result"),
    url(
        r'^filterallproductsASC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_tsv_ASC, name="Search Result"),
    url(
        r'^filterallproductsDESC/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_tsv_DESC, name="Search Result"),
    url(
        r'^filterallproductsbestmatch/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_Ilike, name="Search Result"),

    url(
        r'^filterallproductsexact/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_tsv, name="Search Result"),


    url(
        r'^filterallproducts/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_tsv_new, name="Search Result"),

    url(
        r'^filterallproducts_nazir/(?P<query>.+)/$',
        APIS.FilterAllProducts_Search_Similar_Ilike_nazir, name="Search Result"),


    url(
        r'^filterallproductsnewvector/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_tsv_new_vector, name="Search Result"),


    url(
        r'^filterallproductsCount/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Count, name="Search Result"),


    url(
        r'^filterallproductstsvtri/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$',
        APIS.FilterAllProducts_Search_Similar_tsvtri, name="Search Result"),
    # url(r'^filterallproductsnew/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$', APIS.FilterAllProducts_Search_Similar_Ilike_without_count, name="Search Result"),

    # url(r'^filterallproductstemp/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$', APIS.FilterAllProducts_Search_Similar_Ilike_Faster, name="Search Result"),
    # url(r'^filterallproductssim/(?P<query>.+)/(?P<price1>.+)/(?P<price2>.+)/(?P<brand>.+)/(?P<merchant>.+)/(?P<category>.+)/$', APIS.FilterAllProducts_Search_Similar_S, name="Search Result"),

    url(
        r'^filterproductComparison/(?P<query>.+)/$',
        APIS.Product_Detail_Similarity_test1, name="Search Result"),
    url(
        r'^Product_Detail_Similarity_test/(?P<query>.+)/$',
        APIS.Product_Detail_Similarity_test, name="Search Result1"),

    #####################################################################################################
    # url(r'^filter_deal_comparison/(?P<query>.+)/$',APIS.filter_deal_comparison, name="Search Result1"),
    # url(r'^filter_deal_comparison_test/(?P<query>.+)/$',APIS.filter_deal_comparison_test.as_view(), name="Search Result1"),
    # url(r'^filter_deal_comparison_test/',APIS.filter_deal_comparison_test.as_view(), name="Search Result1"),
    # url(r'^filter_deal_comparison_test/(?P<category>.+)/(?P<query>.+)/$',APIS.filter_deal_comparison_test.as_view(), name="Search Result1"),
    # url(r'^filter_deal_comparison_test/(?P<category>.+)/$',APIS.filter_deal_comparison_test.as_view(), name="Search Result1"),
    url(r'^filter_deal_comparison_test/(?P<typ>.+)/(?P<id>.+)/$',APIS.filter_deal_comparison_test.as_view(), name="Search Result1"),
    #####################################################################################################


    url(
        r'^filter_vocation_comparison/(?P<query>.+)/$',
        APIS.vocation_comparison, name="Search Result_vocation"),
    url(
        r'^sim_test/(?P<query>.+)/$',
        APIS.sim_test, name="Search Result1"),
    url(
        r'^mainsearch/(?P<que>.+)/(?P<items>.+)/$',
        APIS.xxmainsearch, name="Search Result"),
    url(
        r'^mainsearch1/(?P<que>.+)/(?P<items>.+)/$',
        APIS.mainsearch1, name="Search Result"),
    url(
        r'^mainsearch_slides/(?P<query>.+)/$',
        APIS.mainsearch_slides, name="Search Result"),
    url(
        r'^mainsearchincat/(?P<cat>.+)/(?P<query>.+)/$',
        APIS.mainsearchincat, name="Search Result"),
    url(
        r'^mainsearchvector/(?P<query>.+)/(?P<totalResult>.+)/$',
        APIS.mainsearchvector, name="Search Result"),
    url(
        r'^filterproductComparison_mobile/(?P<query>.+)/$',
        APIS.Product_Detail_Similarity_mobile, name="Search Result"),

    url(r'^GetAllCategories$', APIS.GetDistinctCategories, name="Search Result"),
    url(r'^GetAllShops$', APIS.GetDistinctShops, name="Search Result"),

    url(r'^countQuery/(?P<query>.+)/$', APIS.CountQueryAll_new_count, name="Search Result"),
    url(r'^countQuerytemp/(?P<query>.+)/$', APIS.CountQueryAll_new, name="Search Result"),
    url(
        r'^testsearch/(?P<que>.+)/(?P<items>.+)/$',
        APIS.xxtestsearch, name="Search Result"),

]
