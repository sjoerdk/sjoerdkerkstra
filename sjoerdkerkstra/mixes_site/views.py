from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response,get_object_or_404

from mixes_site.models import Mixclouditem


def home(request):
    return render_to_response("mixes_site/base.html")
    #return HttpResponse("MIXES")


def mainpage(request):
    mixes = Mixclouditem.objects.all()
    return render_to_response("mixes_site/mainpage.html",{"mixes":mixes})
