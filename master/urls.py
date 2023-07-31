from django.urls import path
from .import views
app_name='master'

urlpatterns=[
  path('home',views.index,name='home'),
  path('appro',views.approve,name='appro')

]