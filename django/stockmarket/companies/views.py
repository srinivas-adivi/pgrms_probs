"""
Views for the companies app.
"""
import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from django.core import serializers

from companies.models import Company
from stocks.models import Stock 

# Create your views here.
def companies_view(request):
    """A view details of all companies in group."""
    if request.method == 'GET':

        # GET returns a list of objects in json format
        companies = Company.objects.all()
        return render_to_response('companies.json', {'companies': companies},
                                  content_type='application/json')

    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

def company_details(request, code):
    """Company details of given company code in json format """
    try:
        company = Company.objects.get(code=code)
    except Company.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':

        # GET returns a json format
        return render_to_response('company.json', {'company': company},
                                  content_type='application/json')
        
    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

def company_stock_details(request, code, startD, endD=None):
    """Stock details for given company code on/between given day/range in json format"""
    startD = startD[-4:]+'-'+startD[2:4]+'-'+startD[:2]
    endD = endD and endD[-4:]+'-'+endD[2:4]+'-'+endD[:2] or startD
    stocks = Stock.objects.filter(company=code, date__range=(startD, endD)).order_by('date')
    if request.method == 'GET':
        
        # GET returns a json format
        return render_to_response('stocks.json', {'stocks': stocks},
                                  content_type='application/json')
    
    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

def company_stocks_graph(request, code, startD, endD=None):
    """Graphical output of stock details for given company code in between given date range"""
    stocks = json.loads(company_stock_details(request, code, startD, endD).content)
    stocks_as_json = json.dumps(stocks)
    company_name = stocks and json.dumps(stocks[0]['name'].strip()) or ''
    
    if request.method == 'GET':
        
        # GET returns a graph 
        return render_to_response('company_stocks_graph.html', 
						{"company_name": company_name, "data": stocks_as_json},
						content_type='application/xhtml+xml')

    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

