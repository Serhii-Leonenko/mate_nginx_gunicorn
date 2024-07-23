from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from kitchen.models import DishType, Dish, Cook
from kitchen.forms import DishSearchForm, DishTypeSearchForm, CookSearchForm

DISH_TYPE_LIST_URL = reverse("kitchen:dish-type-list")
DISH_LIST_URL = reverse("kitchen:dish-list")
COOK_LIST_URL = reverse("kitchen:cook-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="1qazcde3",
        )
        self.client.force_login(self.user)
        DishType.objects.create(name="Pasta")
        DishType.objects.create(name="Salad")

    def test_retrieve_dish_types(self):
        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types))
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")

    def test_search_dish_type(self):
        response = self.client.get(DISH_TYPE_LIST_URL, {"name": "Pasta"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pasta")
        self.assertNotContains(response, "Salad")


class PublicDishTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="1qazcde3",
        )
        self.client.force_login(self.user)
        self.dish_type = DishType.objects.create(
            name="Salad",
        )
        Dish.objects.create(
            name="Cesar",
            dish_type=self.dish_type,
            price=5.99,
            description="tasty"
        )
        Dish.objects.create(
            name="Olivie",
            dish_type=self.dish_type,
            price=2.99,
            description="tasty"
        )

    def test_retrieve_dishes(self):

        response = self.client.get(DISH_LIST_URL)
        self.assertEqual(response.status_code, 200)
        dishes = Dish.objects.select_related("dish_type").all()
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")

    def test_search_dish(self):

        response = self.client.get(DISH_LIST_URL, {"name": "Cesar"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cesar")
        self.assertNotContains(response, "Olivie")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get(COOK_LIST_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateCookTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="1qazcde3",
        )
        self.client.force_login(self.user)
        Cook.objects.create(username="cook1", years_of_experience=1)
        Cook.objects.create(username="cook2", years_of_experience=12)

    def test_retrieve_cooks(self):
        response = self.client.get(COOK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        cooks = Cook.objects.all()
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_search_cook(self):
        response = self.client.get(COOK_LIST_URL, {"username": "cook1"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "cook1")
        self.assertNotContains(response, "cook2")


class PrivateIndexViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="user",
            password="1qazcde3",
        )
        self.client.force_login(self.user)

    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")
        self.assertIn("num_cooks", response.context)
        self.assertIn("num_dishes", response.context)
        self.assertIn("num_dish_types", response.context)
        self.assertIn("num_visits", response.context)

    def test_index_view_increment_visits(self):
        session = self.client.session
        session["num_visits"] = 5
        session.save()
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.context["num_visits"], 6)