from django.urls import path
from . import views

urlpatterns = [
    path('added/<product_id>', views.add_to_cart, name='add_to_cart')
]
