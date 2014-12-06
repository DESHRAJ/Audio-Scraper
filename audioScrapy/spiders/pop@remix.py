# zz = 0
from scrapy.spider import Spider
from scrapy.selector import Selector
from audioScrapy.items import *
from djangoaudio.models import * 
import numpy as np
import sys
sys.path.append('/home/deshraj/Documents/audioScraper/djangoaudio')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoaudio.settings'

class getNewMovies(Spider):
	name = "pop@remix"
	start_urls = (
		# 'http://www.songspk.name/indian_pop_remix_songs.html',
		'http://www.songspk.name/indian_pop_remix_songs_1.html',
		'http://www.songspk.name/indian_pop_remix_songs_2.html',
		'http://www.songspk.name/indian_pop_remix_songs_3.html',
		)
	def parse(self,response):
		# zz=0
		sel = Selector(response)
		f = open('/home/deshraj/file.txt','a')
		f.write('\n')
		# a = response.xpath('//li/ul/li/a/@href').extract()
		a = response.xpath('//table[@id="table190"]//td/p/a/@href').extract()
		for i in a:
			print "http://songspk.name/"+str(i)
			f.write("'"+"http://songspk.name/"+str(i)+"',\n")
		f.close()
		# item = pksongs()
		# # if response.xpath('//table[@id="table130"]//td/a/text()').extract() is []:
		# songName = response.xpath('//li/div/p/b/a/text()').extract()
		# url = response.xpath('//li/div/a/@href').extract()
		# author = response.xpath('//li/div/p/i/text()').extract()
		# title = response.xpath('//li/div/h1/text()').extract()
		# else:
		# 	songName = response.xpath('//table[@id="table130"]//td/a/text()').extract()
		# 	url = response.xpath('//table[@id="table190"]//tr/td//a/@href').extract()
		# 	author = response.xpath('//table[@id="table131"]//tr/td/p/font/b/text()').extract()
		# 	title = response.xpath('//table[@id="table131"]//tr/td/p/font/b/text()').extract()
			# ziplink = response.path('//li/div/a/center/b/@href').extract()
		# for i in sel, j in songName, k in author:
		# colllection = numpy.column_stack(songName,url,author)
		# # try:
		# for i,j,k in zip(songName,url, author):
		# 	# print i
		# 	# print j
		# 	# print k
		# 	item['title'] = str(title) 
		# 	item['songName'] = str(i)
		# 	item['url'] = str(j)
		# 	item['author'] = str(k)
		# # print zz,"\n \n "
		# # zz = zz+1
		# 	item.save()
			# yield item
			# songs(songName = i,url = j, author = k, title = title).save()
		# except:
			# print "error is there"