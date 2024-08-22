from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.functional import cached_property
from django.db import models


class ShardedModel(models.Model):
    shard_key = models.CharField(max_length=128)

    class Meta:
        abstract = True

    @classmethod
    def shard(cls, shard_key):
        if shard_key is None:
            raise ValueError('Shard key must not be None')
        obj = cls()
        obj.shard_key = shard_key
        return obj

    @cached_property
    def shard_model(self):
        return type(self).get_shard_model(self.shard_key)

    @classmethod
    def get_shard_model(cls, shard_key):
        raise NotImplementedError('Subclasses must implement get_shard_model')

    @classmethod
    def _get_shard_queryset(cls, shard_key):
        return cls.get_shard_model(shard_key).objects.all()

    objects = models.Manager()

    def save(self, **kwargs):
        if not self.pk:
            self.pk = self.shard_model.objects.values_list('pk', flat=True).order_by('-pk').first() or 1
        super().save(**kwargs)


class ShardedByCategoryModel(ShardedModel):
    category_length = 10

    class Meta:
        abstract = True

    SNR_Category = models.CharField(max_length=128)

    @classmethod
    def get_shard_model(cls, shard_key):
        return type(cls)('{}_{}'.format(cls.__name__, shard_key))

    @classmethod
    def get_shard_key(cls, category):
        return str(category[:cls.category_length]).lower
