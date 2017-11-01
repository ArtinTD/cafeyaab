from django.conf.urls import url
from cafe.views import HomePageView, UserInfoView, LoginView
from . import views

urlpatterns = [
    url(r'^$', LoginView.as_view(), name='login'),
    url(r'index/$', HomePageView.as_view(), name='index'),
    url(r'^signup/$', UserInfoView.as_view(), name='signup'),
    # url(r'^$', views.index, name='index'),
]