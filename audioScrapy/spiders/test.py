# zz = 0
from scrapy.spider import Spider
from scrapy.selector import Selector
from audioScrapy.items import *
from djangoaudio.models import * 
import numpy as np
import sys
import re
sys.path.append('/home/deshraj/Documents/audioScraper/djangoaudio')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoaudio.settings'

class getNewMovies(Spider):
	handle_httpstatus_list = [301, 302, 303]
	name = "test"

	start_urls = (
				'http://songspk.name/indian-mp3-songs/creature-3d-2014-mp3-songs.html',
				'http://songspk.name/everybody_on_dance_floor8.html',
				'http://songspk.name/bullet_1976.html',
				)
	def parse(self,response):
		# handle_httpstatus_list = [301, 302, 303]
		# zz=0
		sel = Selector(response)
		item = pksongs()
		# print response.xpath('//table[@id="table130"]//td/a/text()').extract()
		# print "hola hola hola " 
		if len(response.xpath('//table[@id="table130"]//td/a/text()').extract()) is 0:
			songName = response.xpath('//li/div/p/b/a/text()').extract()
			url = response.xpath('//li/div/p/b/a/@href').extract()
			author = response.xpath('//li/div/p/i/text()').extract()
			title = response.xpath('//li/div/h1/text()').extract()
			# print title
			# print songName
			# print url 
			# print author
		else:
			songName = response.xpath('//table[@id="table130"]//td/a/text()').extract()
			url = response.xpath('//table[@id="table190"]//tr/td//a/@href').extract()
			author = response.xpath('//table[@id="table131"]//tr/td/p/font/b/text()').extract()
			title = response.xpath('//table[@id="table131"]//tr/td/p/font/b/text()').extract()
		# 	# ziplink = response.path('//li/div/a/center/b/@href').extract()
		# for i in sel, j in songName, k in author:
		# colllection = numpy.column_stack(songName,url,author)
		# try:
		title = str(title[0])
		title = title.replace(' \n\t\t\t\t\t\t',' ')
		title = title.replace('\n\t\t\t\t\t\t',' ')
		# title = title[3:-2]
		title = re.sub(' +',' ',title)
		for authors in author:
			authors = str(authors)
			authors = authors.replace(' \n\t\t\t\t\t\t',' ')
			# authors = authors.replace('\\t','')
			# authors = authors[3:-2]
			authors = re.sub(' +',' ',authors)
		# xx = 0
		# f = open('newSongsList1.txt','a')
		# print title
		# print songName
		# print url 
		# print author
		if len(author)==1:
			for i,j in zip(songName,url):
				print str(title)
				# print "-------------------------------------"
				# i = re.sub(' +',' ',i)
				print str(i)
				# print "-------------------------------------"
				print str(j)
				# print "-------------------------------------"
			# 	# # print xx
			# 	# # xx = xx+1
				print str(author)
				# print "***************************************"

		else:
			for i,j,k in zip(songName,url,author):
				print str(title)
				# print "-------------------------------------"
				i = re.sub(' +',' ',i)
				print str(i)
				# print "-------------------------------------"
				print str(j)
				# print "-------------------------------------" 	
			# # print xx
			# 	# # xx = xx+1
				print str(k)		# 	print 
				# print "***************************************"

		# 	print 
			# item['title'] = str(title) 
			# item['songName'] = str(i)
			# item['url'] = str(j)
			# item['author'] = str(k)
			# f.write(title+","+i+","+j+","+k+"\n")
			# item.save()
		# print zz,"\n \n "
		# zz = zz+1
			# yield item
			# songs(songName = i,url = j, author = k, title = title).save()
		# except:
			# print "error is there"