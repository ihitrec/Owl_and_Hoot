from django.urls import path
from . import views

urlpatterns = [
    path('<category>/', views.categories, name='categories'),
    path('add/product/', views.add_product, name='add_product'),
    path('edit/<product_id>/', views.edit_product, name='edit_product'),
]
