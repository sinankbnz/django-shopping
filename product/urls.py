from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.login,name='login'),
    path('blogsingle/',views.blogsingle,name='blogsingle'),
    path('blog/',views.blog,name='blog'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact-us/',views.contact,name='contact-us'),
    path('product/<int:id>/',views.product,name='product'),
    path('shop/',views.shop,name='shop'),
    path('register/',views.register,name='register'),


    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
]