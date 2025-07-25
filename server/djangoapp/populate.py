from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {
            "name": "NISSAN",
            "description": "Great cars. Japanese technology"
        },
        {
            "name": "Mercedes",
            "description": "Great cars. German technology"
        },
        {
            "name": "Audi",
            "description": "Great cars. German technology"
        },
        {
            "name": "Kia",
            "description": "Great cars. Korean technology"
        },
        {
            "name": "Toyota",
            "description": "Great cars. Japanese technology"
        },
        {
            "name": "Dodge",
            "description": "American muscle and utility vehicles"
        },
        {
            "name": "Honda",
            "description": "Reliable and efficient Japanese cars"
        },
    ]

    car_make_instances = {}
    for data in car_make_data:
        car_make = CarMake.objects.create(
            name=data["name"],
            description=data["description"]
        )
        car_make_instances[data["name"]] = car_make

    car_model_data = [
        # NISSAN
        {
            "name": "Pathfinder",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["NISSAN"]
        },
        {
            "name": "Qashqai",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["NISSAN"]
        },
        {
            "name": "XTRAIL",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["NISSAN"]
        },
        {
            "name": "Altima",
            "type": "Sedan",
            "year": 2021,
            "car_make": car_make_instances["NISSAN"]
        },

        # Mercedes
        {
            "name": "A-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Mercedes"]
        },
        {
            "name": "C-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Mercedes"]
        },
        {
            "name": "E-Class",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Mercedes"]
        },

        # Audi
        {
            "name": "A4",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Audi"]
        },
        {
            "name": "A5",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Audi"]
        },
        {
            "name": "A6",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Audi"]
        },

        # Kia
        {
            "name": "Sorrento",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Kia"]
        },
        {
            "name": "Carnival",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Kia"]
        },
        {
            "name": "Cerato",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances["Kia"]
        },

        # Toyota
        {
            "name": "Corolla",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances["Toyota"]
        },
        {
            "name": "Camry",
            "type": "Sedan",
            "year": 2023,
            "car_make": car_make_instances["Toyota"]
        },
        {
            "name": "Kluger",
            "type": "SUV",
            "year": 2023,
            "car_make": car_make_instances["Toyota"]
        },

        # Dodge
        {
            "name": "Durango",
            "type": "SUV",
            "year": 2014,
            "car_make": car_make_instances["Dodge"]
        },

        # Honda
        {
            "name": "Accord",
            "type": "Sedan",
            "year": 2020,
            "car_make": car_make_instances["Honda"]
        },
    ]

    for data in car_model_data:
        CarModel.objects.create(
            name=data["name"],
            car_make=data["car_make"],
            type=data["type"],
            year=data["year"]
        )
