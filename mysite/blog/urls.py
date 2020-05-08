 

from . import views
from django.urls import path,include
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('contact/',views.contact_form,name='contact'),
    path('signup/',views.signup,name='signup')
     
]
