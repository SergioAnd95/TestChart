from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse

from .models import Group, Chart
from .forms import ChartFilterForm

# Create your views here.
import json


def index(request):
    """
    display main page
    :param request: HttpRequest
    :return: HttpResponse
    """
    return render(request, 'index.html', {'chartfilter': ChartFilterForm()})


def chart_build(request, group_id=None):
    """
    get json data
    :param request: HttpRequest
    :param group_id: int
    :return: HttpResponse
    """
    if request.is_ajax():
        print('ajax')
        if group_id:
            region = get_object_or_404(Group, pk=group_id)
            charts = Chart.objects.filter(region=region)
        else:
            charts = Chart.objects.all()
        outgoing_list = {chart.param: chart.value for chart in charts}

        return HttpResponse(json.dumps(outgoing_list))