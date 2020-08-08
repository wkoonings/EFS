from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from . import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

api_urlpatterns = [
    path('auth/', obtain_jwt_token),
    path('', views.api_customer_list),
    url(r'^customers/$', views.api_customer_list),
    url(r'^customers/(?P<pk>[0-9]+)$', views.api_get_customer),
    path('investements/', views.api_investment_list),
    url(r'^investments/$', views.api_investment_list),
    url(r'^investments/(?P<pk>[0-9]+)$', views.api_get_investment),
    path('stocks/', views.api_stock_list),
    url(r'^stocks/$', views.api_stock_list),
    url(r'^stocks/(?P<pk>[0-9]+)$', views.api_get_stock)
]

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    url(r'^customers_json/', views.CustomerList.as_view()),
    path('api/v1/', include(api_urlpatterns))
]

urlpatterns = format_suffix_patterns(urlpatterns)