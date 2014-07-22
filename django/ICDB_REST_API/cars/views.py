"""
Views for the cars app.
"""
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import HttpResponseNotAllowed
from django.shortcuts import render_to_response
from cars.models import Car
from cars.forms import CarForm


def cars_view(request):
    """A view for cars."""
    if request.method == 'POST':
        # POST creates a car
        try:
            data = json.loads(request.body)
        except ValueError:
            return HttpResponseBadRequest('Not valid JSON!')

        form = CarForm(data)

        if form.is_valid():
            car = form.save()

            # Return a 201 CREATED response
            response = HttpResponse(status=201)
            response['Location'] = '/cars/' + str(car.id)

            return response
        else:
            return HttpResponseBadRequest('Invalid data!')
    elif request.method == 'GET':
        # GET returns a list of objects
        cars = Car.objects.all()
        return render_to_response('cars.json', {'cars': cars},
                                  content_type='application/json')

    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET', 'POST'])

def car_details(request, pk):
    """Retrieve, update or delete a car details"""
    try:
        car = Car.objects.get(id=int(pk))
    except Car.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        # GET returns a car object with given id
        return render_to_response('car.json', {'car': car},
                                  content_type='application/json')
    elif request.method == 'DELETE':
        # DELETE a car object
        car.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        # PUT updates the details of existing car
        try:
            data = json.loads(request.body)
        except ValueError:
            return HttpResponseBadRequest('Not valid JSON!')

        form = CarForm(data)

        if form.is_valid():
            car.make = data.get('make', car.make)
            car.model = data.get('model', car.model)
            car.year = data.get('year', car.year)
            car.save()

            # Return a 205 CREATED response
            response = HttpResponse(status=205)
            response['Location'] = '/cars/' + str(car.id)

            return response
        else:
            return HttpResponseBadRequest('Invalid data!')
        
    # Notify client of supported methods
    return HttpResponseNotAllowed(['GET', 'DELETE', 'PUT'])

