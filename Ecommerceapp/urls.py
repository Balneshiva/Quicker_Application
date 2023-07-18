from django.urls import path,include
from Ecommerceapp import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('contact',views.contact,name = "contact"),
    path('about',views.about,name = "about"),
    path('checkout/',views.checkout,name = "Checkout"),
    path('blog',views.blog,name = "blog"),
    # path('profile',views.profile, name = "Checkout")
    #path('handlerequest/', views.handlerequest, name="HandleRequest"),
]