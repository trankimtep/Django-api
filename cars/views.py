from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Car

def get_cars(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        car_data = {
            'make': car.make,
            'model': car.model,
            'year': car.year,
            'price': car.price,
        }
        car_list.append(car_data)
    return JsonResponse(car_list, safe=False)

@csrf_exempt
def create_car(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        make = data.get('make')
        model = data.get('model')
        year = data.get('year')
        price = data.get('price')
        
        car = Car(make=make, model=model, year=year, price=price)
        car.save()
        
        return JsonResponse({'message': 'Car created successfully'}, status=201)
