# from haystack import indexes
#
# from laptop.models import Laptop_DB
#
# class laptop_index(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#
#     def get_model(self):
#         return Laptop_DB
#
#     def index_queryset(self, using=None):
#         """Used when the entire index for model is updated."""
#         return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())