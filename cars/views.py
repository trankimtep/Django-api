from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Car

def get_cars(request):
    cars = Car.objects.all()
    car_list = []
    for car in cars:
        car_data = {
            'id': car.id,
            'make': car.make,
            'model': car.model,
            'year': car.year,
            'price': car.price,
        }
        car_list.append(car_data)
    return JsonResponse(car_list, safe=False, status=200)

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

        return JsonResponse({'id': car.id, 'message': 'Car created successfully'}, status=201)

    
@csrf_exempt
def update_or_delete_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return JsonResponse({'message': 'Car not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        car.make = data.get('make', car.make)
        car.model = data.get('model', car.model)
        car.year = data.get('year', car.year)
        car.price = data.get('price', car.price)
        car.save()
        return JsonResponse({'message': 'Car updated successfully'})

    elif request.method == 'DELETE':
        car.delete()
        return JsonResponse({'message': 'Car deleted successfully'})

    # Return a 405 Method Not Allowed response for other HTTP methods
    return JsonResponse({'message': 'Method not allowed'}, status=405)



