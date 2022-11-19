from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    subtitle= models.CharField(max_length=200, verbose_name="subtitle")
    content = models.CharField(max_length=600, verbose_name="content")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="creation date")
    updated = models.DateTimeField(auto_now=True, verbose_name="update date")
    
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ["-updated"]
        
    def __str__(self):
        return self.title
