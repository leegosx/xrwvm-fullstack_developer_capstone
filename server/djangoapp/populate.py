from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "price": 35000.00, "car_make": car_make_instances[0]},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "price": 28000.00, "car_make": car_make_instances[0]},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "price": 30000.00, "car_make": car_make_instances[0]},
        {"name": "A-Class", "type": "SUV", "year": 2023, "price": 32000.00, "car_make": car_make_instances[1]},
        {"name": "C-Class", "type": "SUV", "year": 2023, "price": 36000.00, "car_make": car_make_instances[1]},
        {"name": "E-Class", "type": "SUV", "year": 2023, "price": 55000.00, "car_make": car_make_instances[1]},
        {"name": "A4", "type": "SUV", "year": 2023, "price": 40000.00, "car_make": car_make_instances[2]},
        {"name": "A5", "type": "SUV", "year": 2023, "price": 42000.00, "car_make": car_make_instances[2]},
        {"name": "A6", "type": "SUV", "year": 2023, "price": 47000.00, "car_make": car_make_instances[2]},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "price": 29000.00, "car_make": car_make_instances[3]},
        {"name": "Carnival", "type": "SUV", "year": 2023, "price": 31000.00, "car_make": car_make_instances[3]},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "price": 20000.00, "car_make": car_make_instances[3]},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "price": 23000.00, "car_make": car_make_instances[4]},
        {"name": "Camry", "type": "Sedan", "year": 2023, "price": 27000.00, "car_make": car_make_instances[4]},
        {"name": "Kluger", "type": "SUV", "year": 2023, "price": 39000.00, "car_make": car_make_instances[4]},
    ]

    for data in car_model_data:
        CarModel.objects.get_or_create(
            name=data['name'], 
            car_make=data['car_make'], 
            type=data['type'], 
            year=data['year'],
            defaults={'price': data['price']}
        )