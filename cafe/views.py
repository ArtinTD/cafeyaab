from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView



class HomePageView(FormView):
    success_url = '/index/'
    form_class = AuthenticationForm
    template_name = 'index.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(HomePageView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(HomePageView, self).form_valid(form)

class SignUp