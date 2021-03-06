from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('update/',views.user_update,name='user_update'),
    path('password/',views.user_password,name='user_password'),
    path('orders/',views.user_orders,name='user_orders'),
    path('orders_product/',views.user_orders_product,name='user_orders_product'),
    path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
    path('comments/',views.user_comments,name='user_comments'),
]
