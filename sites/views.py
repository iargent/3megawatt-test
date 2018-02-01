from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Site


def index(request):
    sites_list=Site.objects.all()
    context = {
        'sites_list': sites_list,
    }
    return HttpResponse(render(request, 'sites/index.html', context))

def detail(request, site_id):
    try:
        site = Site.objects.get(pk=site_id)
    except Site.DoesNotExist:
        raise Http404("Site does not exist")
    return render(request, 'sites/detail.html', {'site': site })
