from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from sites.models import Site


def index(request):
    if request.path=='/summary-average/':
        sites_list=Site.avg_by_site()
    else:
        sites_list=Site.sum_by_site()
    context = {'sites_list': sites_list}
    return HttpResponse(render(request, 'summary/index.html', context))
