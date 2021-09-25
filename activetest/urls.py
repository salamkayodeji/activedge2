from django.urls import path, include
from .views import StockList, StockDetail, StockHtmlList, StockHtmlDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()



urlpatterns = [
    path('api/stocks/', StockList.as_view()),
    path('', StockHtmlList.as_view(), name='home'),
    path('<int:pk>', StockHtmlDetail.as_view()),  
    path('api/stocks/<int:pk>/', StockDetail.as_view()),  
]