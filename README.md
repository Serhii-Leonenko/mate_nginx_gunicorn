# Restaurant Kitchen Service

Django project for managing kitchen operations in a restaurant, including managing cooks, dishes, and dish types.


## Installation
Follow these steps to set up the project locally:


Clone the repository and switch to the project directory:
```shell
git clone https://github.com/AntonKorinchuk/restaurant-kitchen-service.git
cd restaurant-kitchen-service
```

Create a virtual environment:
```shell
python -m venv venv
```

Activate the virtual environment:
On Windows:
```shell
 venv\Scripts\activate
 ```
On macOS and Linux:
```shell
source venv/bin/activate
```

Install dependencies:
```shell
pip install -r requirements.txt
```

Apply migrations:
```shell
python manage.py migrate
```

Create a superuser:
```shell
python manage.py createsuperuser
```

Run:
```shell
python manage.py runserver
```



## Key Features:

* Dish Creation:

Cooks can easily create new dishes, providing detailed information.
The system allows for the classification of dishes into various types (Dishtypes), providing a structured organization of the menu.

* Responsibility Assignment:

Cooks can assign specific dishes to themselves or fellow team members, clearly defining responsibilities for each item on the menu.
This feature ensures accountability and a streamlined workflow by assigning cooks to dishes based on their expertise and availability.

* Performance 

The Restaurant Kitchen Service is designed to elevate the efficiency and collaboration within the kitchen, ultimately contributing to the success and reputation of the restaurant. Whether you are a small bistro or a large-scale eatery, this management system aims to be a valuable tool in enhancing the culinary operations of your establishment.
