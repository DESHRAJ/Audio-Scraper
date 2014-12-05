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
	name = "songspk"
	start_urls = (
		'http://www.songspk.name/bollywood-songs-mp3.html',
		'http://www.songspk.name/indian_pop_remix_songs.html',
		'http://www.songspk.name/bhangra_songs.html',
		'http://www.songspk.name/ghazals.html',
		'http://www.songspk.name/artists.html',
		'http://www.songspk.name/bollywood_music_compilations.html',
		'http://www.songspk.name/wedding_songs.html',
		'http://www.songspk.name/audio_single_mp3_songs.html',
		'http://www.songspk.name/audio_single_mp3_songs.html',
		'http://www.songspk.name/bollywood-songs-mp3.html',
		'http://www.songspk.name/pakistani_songs.html',
		'http://www.songspk.name/indian_pop_remix_songs.html',
		'http://www.songspk.name/song-of-the-day-mp3.html',
		'http://www.songspk.name/bhangra_songs.html',
		'http://www.songspk.name/ghazals.html',
		'http://www.songspk.name/artists.html',
		'http://www.songspk.name/old_is_gold_revival.html',
		'http://www.songspk.name/wedding_songs.html',
		'http://www.songspk.name/bollywood_music_compilations.html',
		'http://www.songspk.name/upcoming_music_list.html',
		'http://www.songspk.name/indian-songs-latest.html',
		'http://www.songspk.name/music_reviews.html',
		'http://www.songspk.name/movie_reviews.html',
		'http://www.songspk.name/indian-pop-remix/coke-studio-season-7-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/life-mein-twist-hai-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/pk-2014-mp3-songs.html',
		'http://www.songspk.name/http://www.songspk.name/indian-mp3-songs/zid-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/ungli-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/action-jackson-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/happy-ending-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/kill-dil-2014-mp3-songs.html',
		'http://www.songspk.name/singles/india-re-a-r-rahman-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/sajna-farhan-saeed-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/superman-tevar-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/love-is-waste-of-time-pk-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/saheli-bohemia-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/dance-basanti-ungli-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/monali-trance-shaukeens-honey-singh-2014-download-mp3-song.html',
		'http://www.songspk.name/singles/o-soniye-titoo-mba-2014-download-mp3-song.html',
		'http://www.songspk.name/song-of-the-day/dheere-dheere-dheere-tere-bina-mp3-song-of-day.html',
		'http://www.songspk.name/song-of-the-day/dil-haara-tashan-mp3-song-of-day.html',
		'http://www.songspk.name/song-of-the-day/tum-mile-love-reprise-tum-mile-mp3-song-of-day.html',
		'http://www.songspk.name/song-of-the-day/socha-nahin-tha-kaante-mp3-song-of-day.html',
		'http://www.songspk.name/song-of-the-day/saathiya-tune-kya-kiya-love-mp3-song-of-day.htm',
		'http://www.songspk.name/compilations/soulful-voice-arijit-singh-2014-mp3-songs.html',
		'http://www.songspk.name/bollywood_music_compilations.html',
		'http://www.songspk.name/bhangra/yo-yo-hits-honey-singh-2013-mp3-songs.html',
		'http://www.songspk.name/bollywood_music_compilations.html',
		'http://www.songspk.name/indian-pop-remix/neon-jay-sean-2013-mp3-songs.html',
		'http://www.songspk.name/compilations/kk_best_of_me_vol1_songspk_collection_mp3_songs.html',
		'http://www.songspk.name/bhangra/twelve-bilal-saeed-2011-mp3-songs.html',
		'http://www.songspk.name/compilations/srk_his_journey_for_love_instrumental_disc_1_mp3_songs.html',
		'http://www.songspk.name/indian-pop-remix/coke-studio-season-7-2014-mp3-songs.html',
		'http://www.songspk.name/best_of_abrar_ul_haq.html',
		'http://www.songspk.name/hai_dil_jaani_shazia_manzoor.html',
		'http://www.songspk.name/babia_sajjad_ali.html',
		'http://www.songspk.name/aitebar_vital_signs.html',
		'http://www.songspk.name/indian-mp3-songs/kick-salman-khan-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/raja-natwarlal-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/purani-jeans-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/mary-kom-2014-mp3-songs.html',
		'http://www.songspk.name/indian-mp3-songs/humpty-sharma-ki-dulhania-2014-mp3-songs.html',
		'http://www.songspk.name/indian-pop-remix/back-2-love-rahat-fateh-ali-khan-2014-mp3-songs.html',
		'http://www.songspk.name/indian-pop-remix/dj-dance-remix-vol6-2014-mp3-songs.html',
		'http://www.songspk.name/indian-pop-remix/raastey-shraddha-sharma-2014-mp3-songs.html',
		'http://www.songspk.name/indian-pop-remix/desi-kalakaar-yo-yo-honey-singh-2014-mp3-songs.html',
		'http://www.songspk.name/indian-pop-remix/judah-falak-2013-mp3-songs.html',
		'http://www.songspk.name/jagjit_singh_inteha_2009.html',
		'http://www.songspk.name/parwaaz.html',
		'http://www.songspk.name/mehdi_hassan_vol4.html',
		'http://www.songspk.name/ishq_nachaye.html',
		'http://www.songspk.name/rabba_yaar_milade.html',
		'http://www.songspk.name/bhangra/yo-yo-hits-honey-singh-2013-mp3-songs.html',
		'http://www.songspk.name/bhangra/punjabi-hits-2014-mp3-songs.html',
		'http://www.songspk.name/bhangra/jatt-james-bond-2014-mp3-songs.html',
		'http://www.songspk.name/bhangra/this-party-gettin-hot-2014-mp3-songs.html',
		'http://www.songspk.name/bhangra/heer-2014-mp3-songs.html',
		'http://songspk.name/indian-mp3-songs/haider-2014-mp3-songs.html',
		'http://songspk.name/indian-pop-remix/raja-natwarlal-2014-mp3-songs.html',
		'http://songspk.name/indian-mp3-songs/singham-retuns-singham2-2014-mp3-songs.html',
		)
	def parse(self,response):
		# zz=0
		sel = Selector(response)
		item = pksongs()
		# if response.xpath('//table[@id="table130"]//td/a/text()').extract() is []:
		songName = response.xpath('//li/div/p/b/a/text()').extract()
		url = response.xpath('//li/div/a/@href').extract()
		author = response.xpath('//li/div/p/i/text()').extract()
		title = response.xpath('//li/div/h1/text()').extract()
		# else:
		# 	songName = response.xpath('//table[@id="table130"]//td/a/text()').extract()
		# 	url = response.xpath('//table[@id="table190"]//tr/td//a/@href').extract()
		# 	author = response.xpath('//table[@id="table131"]//tr/td/p/font/b/text()').extract()
		# 	title = response.xpath('//table[@id="table131"]//tr/td/p/font/b/text()').extract()
			# ziplink = response.path('//li/div/a/center/b/@href').extract()
		# for i in sel, j in songName, k in author:
		# colllection = numpy.column_stack(songName,url,author)
		# try:
		for i,j,k in zip(songName,url, author):
			# print i
			# print j
			# print k
			item['title'] = str(title) 
			item['songName'] = str(i)
			item['url'] = str(j)
			item['author'] = str(k)
		# print zz,"\n \n "
		# zz = zz+1
			item.save()
			# yield item
			# songs(songName = i,url = j, author = k, title = title).save()
		# except:
			# print "error is there"