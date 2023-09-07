from django.contrib import admin
from django.urls import path
from authcart import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup,name='signup'),
    path('login/',views.handlelogin,name='handlelogin'),
    path('logout/',views.handlelogout,name='handlelogout'),
]
