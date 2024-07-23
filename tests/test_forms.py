from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.forms import (
    DishForm,
    CookCreationForm,
    CookYearsOfExperienceUpdateForm,
    CookSearchForm,
    DishSearchForm,
    DishTypeSearchForm,
)
from kitchen.models import DishType, Dish


class FormsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="cook",
            password="1qazcde3",
            years_of_experience=2,
        )
        self.dish_type = DishType.objects.create(
            name="Salad",
        )
        self.dish = Dish.objects.create(
            name="Olivie",
            dish_type=self.dish_type,
            price=2.99,
            description="tasty"
        )

    def test_dish_form_is_valid(self):
        form_data = {
            "name": "cesar",
            "price": 2.99,
            "description": "tasty",
            "dish_type": self.dish_type.id,
            "cook": [self.user.id]
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "cesar")
        self.assertEqual(form.cleaned_data["price"], Decimal('2.99'))
        self.assertEqual(form.cleaned_data["description"], "tasty")
        self.assertEqual(form.cleaned_data["dish_type"], self.dish_type)
        self.assertEqual(list(form.cleaned_data["cook"]), [self.user])


    def test_cook_creation_form_is_valid(self):
        form_data = {
            "username": "cook1",
            "password1": "cook12test",
            "password2": "cook12test",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": 2,
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "cook1")

    def test_cook_creation_form_invalid_years_of_experience(self):
        form_data = {
            "username": "cook",
            "password1": "cook12test",
            "password2": "cook12test",
            "first_name": "First",
            "last_name": "Last",
            "years_of_experience": -2,
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)

    def test_years_of_experience_update_form_is_valid(self):
        form_data = {"years_of_experience": 3}
        form = CookYearsOfExperienceUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["years_of_experience"], 3)

    def test_years_of_experience_update_form_invalid(self):
        form_data = {"years_of_experience": -10}
        form = CookYearsOfExperienceUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("years_of_experience", form.errors)

    def test_cook_search_form_is_valid(self):
        form_data = {"username": "cook"}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "cook")

    def test_cook_search_form_empty_username_is_valid(self):
        form_data = {"username": ""}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["username"], "")

    def test_dish_search_form_is_valid(self):
        form_data = {"name": "cesar"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "cesar")

    def test_dish_type_search_form_is_valid(self):
        form_data = {"name": "Salad"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "Salad")

