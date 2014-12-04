# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.contrib.djangoitem import DjangoItem
from djangoaudio.models import * 

class AudioscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class Hk0WeatherItem(Item):
#   time = Field()
#   station = Field()
#   ename = Field()
#   cname = Field()
#   temperture = Field()
#   humidity = Field()

# class Hk0RegionalItem(DjangoItem):
#   django_model = WeatherData

# class Hk0TropicalItem(Item):
#   time = Field()
#   postime = Field()
#   x = Field()
#   y = Field()
#   category = Field()
#   windspeed = Field()
#   tctype = Field()

# class Hk0RainfallItem(DjangoItem):
#   django_model = RainfallData

# class ReportItem(DjangoItem):
#   django_model = ReportData 
