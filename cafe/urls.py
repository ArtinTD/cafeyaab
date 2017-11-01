from django.conf.urls import url
from cafe.views import HomePageView
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='login'),
    # url(r'^$', views.index, name='index'),
]