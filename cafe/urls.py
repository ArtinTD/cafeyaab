from django.conf.urls import url
from cafe.views import HomePageView, LoginView
from . import views

urlpatterns = [
    url(r'login/^$', LoginView.as_view(), name='login'),
    url(r'index/$', HomePageView.as_view(), name='index'),
    # url(r'^$', SignupView.as_view(), name='signup'),
    url(r'^$', views.signup, name='signup'),
]