from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string, get_template
import random,string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import json
import datetime
import md5
import string
import random
import urllib2
import os
import json as simplejson
import sys, os
import mongoengine
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import csv
sys.path.append('/home/deshraj/Documents/audioScraper/djangoaudio/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangoaudio.settings'
from djangoaudio.models import * 
# _MONGODB_DATABASE_HOST = \
# 	   'mongodb://%s:%s@%s/%s' \
# 	   % ('fratmart', 'fratmartdb', 'localhost', 'admin')
# mongoengine.connect('admin', host=_MONGODB_DATABASE_HOST)
f = open('songslist.csv', 'r')
i=0
r = csv.reader(f)
for row in r :
	if(i>=667):
		try:
		# title = row[0]
			print i
			songs.objects.create(title = row[0], songName=row[1],url = row[2],author = row[3]).save()
			print "success " + row[1]
		except:
			print "error "+ row[1]
	i = i+1


# finally:	
# f.close()