from django.conf.urls import url
from cafe.views import HomePageView, SignUpView
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    # url(r'^$', views.index, name='index'),
]