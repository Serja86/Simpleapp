from django.urls import path
# Импортируем созданное нами представление
from .views import (
   ProductsList, ProductDetail, create_prouct, ProductCreate, multiply
)

urlpatterns = [
   path('multiply/', multiply),
   path('', ProductsList.as_view()),
   path('<int:pk>', ProductDetail.as_view()),
   path('', include('multiply.urls')),
   path('create/', ProductCreate.as_view(), create_prouct, name='product_create'),
]