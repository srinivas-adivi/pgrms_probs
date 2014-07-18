"""
Views for the companies app.
"""
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from companies.models import Company
from stocks.models import Stock 

# Create your views here.
def companies_view(request):
    """A view for companies."""
    if request.method == 'GET':
        # GET returns a list of objects
        companies = Company.objects.all()
        return render_to_response('companies.json', {'companies': companies},
                                  content_type='application/json')

    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

def company_details(request, code):
    """Retrieve stock details"""
    try:
        company = Company.objects.get(code=code)
    except Company.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        # GET returns a stock object with given id
        return render_to_response('company.json', {'company': company},
                                  content_type='application/json')
        
    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

def company_stock_details(request, code, startD, endD=None):
    """Retrieve stock details"""
    try:
        startD = startD[-4:]+'-'+startD[2:4]+'-'+startD[:2]
        if endD:
            endD = endD[-4:]+'-'+endD[2:4]+'-'+endD[:2]
            stocks = Stock.objects.filter(company=code, date__range=(startD, endD)).order_by('date')[::-1]
        else:
            stocks = Stock.objects.filter(company=code, date=startD)
            
    except Stock.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        # GET returns a stock object with given id
        return render_to_response('stocks.json', {'stocks': stocks},
                                  content_type='application/json')
        
    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET'])

