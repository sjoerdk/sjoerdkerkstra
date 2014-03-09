from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response,get_object_or_404


def home(request):
    return render_to_response("sjoerdkerkstra_site/base.html")
    #return render_to_response("base2.html")
    #return HttpResponse("MIXES")
