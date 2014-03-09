from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response,get_object_or_404


def home(request):
    return render_to_response("mixes_site/base.html")
    #return HttpResponse("MIXES")
