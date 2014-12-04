# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
# from scrapy.contrib.djangoitem import DjangoItem
# from djangoaudio.models import * 

class AudioscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class songspk(scrapy.Item):
# 	title = scrapy.Field()
# 	author = scrapy.Field()
# 	songName = scrapy.Field()
# 	ziplink = scrapy.Field()
# 	url = scrapy.Field()

# class songspk(DjangoItem):
# 	django_model = songsPkDb