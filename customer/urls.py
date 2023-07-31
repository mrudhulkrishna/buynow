from django.urls import path
from .import views
app_name='customer'

urlpatterns=[
  path('home',views.index,name='home'),
  path('detail/<int:id>',views.details,name='detail'),
  path('filter/<int:id>',views.filter,name='filter'),
  path('cart',views.cart_view,name='cart'),
  path('addcart<int:product_id>',views.add_cart,name='addcart'),
  path('remove_cart',views.remove_cart,name='remove_cart'),
  path('update_quantity',views.update_quantity,name='update_quantity'),
  path('order_product',views.order_product,name='order_product'),
  path('updatepayment',views.updatepayment,name='updatepayment'),
  path('myorder',views.myorder,name='myorder'),
 
  
]