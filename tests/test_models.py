from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Dish, DishType


class ModelTests(TestCase):

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="salad"
        )
        self.assertEqual(str(dish_type), f"{dish_type.name}")

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="cook",
            password="1qazcde3",
            first_name="Cook",
            last_name="Cookich",
            years_of_experience=2
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="salad"
        )
        dish = Dish.objects.create(
            name="Olivie",
            dish_type=dish_type,
            price=2.99,
            description="tasty"
        )
        self.assertEqual(str(dish), f"{dish.name} {dish.price}")

    def test_create_cook_with_year_of_experience(self):
        username = "cook"
        password = "1qazcde3"
        years_of_experience = 3
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
