from django.conf.urls import url
from django.contrib.auth.views import login, logout
from cafe.views import HomePageView
from . import views

urlpatterns = [
    # url(r'login/$', LoginView.as_view(), name='login'),
    url(r'^index/$', HomePageView.as_view(), name='index'),
    url(r'^login', login, name='login'),
    url(r'^logout', logout, name='logout'),
    # url(r'^$', SignupView.as_view(), name='signup'),
    url(r'^$', views.signup, name='signup'),
]