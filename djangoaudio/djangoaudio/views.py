from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import random,string
from djangoaudio.models import * 


def home(request):
	c = {}
	c.update(csrf(request))
	if request.GET:
		search = request.GET.get('search')
		if search:
			cc1=songs.objects.filter(songName__icontains=search)
			cc2=songs.objects.filter(title__icontains=search)
			cc3=songs.objects.filter(author__icontains=search)
		return render_to_response('result.html',{'cc1':cc1,'cc2':cc2,'cc3':cc3},context_instance=RequestContext(request))
	return render_to_response('index.html')
	# return HttpResponse("<h1>Under Construction... Will be there very soon </h1>")

def songspk(request):
	# a = None
	a = songs.objects.all()
	return render_to_response('songspk.html',{'a':a},context_instance=RequestContext(request))