from django.db import models
from django.contrib import admin
# Create your models here.


class Mixclouditem(models.Model):
    user_name = models.CharField(max_length=200,default="",
                                help_text = "Will be used to generate link url")                                    
    mix_name = models.CharField(max_length=200,default="",
                                help_text = "Name of the mix, no-spaces-but-with-hyphens")    
    description = models.TextField(max_length = 1024, default="",
                                   blank=True,help_text = "Print this below widget")
    


admin.site.register(Mixclouditem)
