from django.urls import path

from . import views


app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/add/', views.PortfolioAddToken.as_view(), name='add'),
    path('portfolio/<str:ticker>/', views.token_detail, name='detail'),
    path(
        'portfolio/<str:ticker>/add-transaction/',
        views.PortfolioAddTransaction.as_view(),
        name='add_transaction'
    ),
]
