from django.urls import path
from .import views
app_name='seller'

urlpatterns=[
   path('home',views.index,name='home'),
   path('product',views.product,name='product'),
   path('stock',views.stock,name='stock'),
   path('category',views.category,name='category'),
   path('addcat',views.addcat,name='addcat'),
   path('edit/<int:id>',views.edit,name='edit'),
   path('proview',views.proview,name='proview'),
   path('delete/<int:id>',views.delete,name='delete'),
   path('proedit/<int:id>',views.proedit,name='proedit'),
   path('prodelete/<int:id>',views.prodelete,name='prodelete'),
   path('orderview',views.orderview,name='orderview'),

]