from django.urls import path

from kitchen.views import index, DishTypeListView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView

urlpatterns = [
    path(
        "",
        index,
        name="index"
    ),
    path(
        "dish_type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish_type/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
]

app_name = "kitchen"
