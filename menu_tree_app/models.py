from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    menu = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url_name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['menu'] 

    def __str__(self):
        return self.menu

    def get_absolute_url(self):
        if self.url_name:
            return reverse(self.url_name)
        return self.url
