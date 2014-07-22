"""
Views for the stocks app.
"""
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from stocks.models import Stock
from stocks.forms import StockForm


def stocks_view(request):
    """A view for stocks."""
    if request.method == 'GET':
        # GET returns a list of objects
        stocks = Stock.objects.all()
        return render_to_response('stocks.json', {'stocks': stocks},
                                  content_type='application/json')

    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

def stock_details(request, code):
    """Retrieve stock details"""
    try:
        stocks = Stock.objects.filter(company=code).order_by('date')[::-1]
    except Stock.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # GET returns a stock object with given id
        return render_to_response('stocks.json', {'stocks': stocks},
                                  content_type='application/json')
        
    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

