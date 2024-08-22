


from django.db import models
from django.utils.functional import cached_property
from django.utils.module_loading import import_string
from django.apps import apps

class ShardedModel(models.Model):
    shard_key = None

    class Meta:
        abstract = True

    @cached_property
    def shard_id(self):
        return str(getattr(self, self.shard_key))

    @classmethod
    def _get_shard_model(cls, **kwargs):
        app_label = cls._meta.app_label
        model_name = cls.__name__
        shard_id = str(kwargs.get(cls.shard_key))

        model_path = f"{app_label}.{model_name}_{shard_id}"
        model = apps.get_model(model_path, model_name)

        return model

    def save(self, *args, **kwargs):
        shard_model = self._get_shard_model()
        shard_model.objects.create(**self.__dict__)
        return super().save(*args, **kwargs)

class Product(ShardedModel):
    SNR_SKU = models.CharField(max_length=50)
    SNR_Title = models.CharField(max_length=255)
    SNR_ModelNo = models.CharField(max_length=50)
    SNR_Brand = models.CharField(max_length=50)
    SNR_UPC = models.CharField(max_length=50)
    SNR_Available = models.BooleanField(default=True)
    SNR_ProductURL = models.URLField(max_length=255)
    SNR_ImageURL = models.URLField(max_length=255)
    SNR_Description = models.TextField()
    SNR_isShow = models.BooleanField(default=True)
    SNR_Date = models.DateTimeField(auto_now_add=True)
    SNR_Category = models.CharField(max_length=50)
    SNR_Condition = models.CharField(max_length=50)
    SNR_PriceBefore = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    SNR_CustomerReviews = models.IntegerField(null=True)
    SNR_Price = models.DecimalField(max_digits=12, decimal_places=2)
    SNR_SubCategory = models.CharField(max_length=50)

    shard_key = 'SNR_Category'

    class Meta:
        unique_together = ['SNR_SKU', 'SNR_Category']
