from django.conf.urls import url
from django.contrib.auth.views import login, logout
from cafe.views import HomePageView,  cafe_view, LoginView, profile_view, ProfileUpdate
from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^index/$', HomePageView.as_view(), name='index'),
    url(r'^edit/$', ProfileUpdate.as_view(), name='edit'),
    #url(r'^(?P<slug>[-\d]+)/$', CafeView.as_view(), name='cafe'),
    url(r'^(?P<slug>[-\d]+)/$', cafe_view, name='cafe'),
    url(r'^user/(?P<slug>[-\d]+)/$', profile_view, name='user'),
    # url(r'^cafe/$', CafeView.as_view(), name='cafe'),
    # url(r'^login', login, name='login'),
    url(r'^logout', logout, name='logout'),
    # url(r'^$', SignupView.as_view(), name='signup'),
    url(r'^$', views.signup, name='signup'),
]