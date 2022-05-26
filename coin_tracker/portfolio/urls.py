from django.urls import path

from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('token-list/', views.token_list, name='token-list'),
    path('token-list/<int:pk>/', views.token_detail, name='token-detail'),
    path('transactions/', views.transactions, name='transactions')
]
