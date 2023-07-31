from django.urls import path
from .import views
app_name='commen'

urlpatterns=[
   path('home',views.index,name='home'),
   path('admin',views.admin,name='admin'),
   path('seller',views.seller,name='seller'),
   path('customer',views.cust,name='customer'),
   path('sell_log',views.sello,name='sell_log'),
   path('cust_log',views.custo,name='cust_log')
]