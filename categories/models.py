from django.db import models

# Create your models here.


class CategoriesBrandNames(models.Model):

    brand_name = models.CharField(max_length=256, db_index=True, default=None, null=True)
    products_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id) if str(self.id) else '' + ' , ' + self.brand_name if self.brand_name else '' + ' , ' + str(self.products_count) if (self.products_count) else ''
