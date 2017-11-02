from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from cafe.forms.user_forms import SignUpForm
from cafe.models import  Cafe
import json
import urllib
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.conf import settings
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# from .models import Comment
# from .forms import CommentForm

from django.views.generic.list import ListView
# from cafe.token import account_activation_token


class HomePageView(ListView):
    model = Cafe
    template_name = 'index.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        cafes = Cafe.objects.filter(name__contains=q)
        return cafes


class ProfileUpdate(UpdateView):
    # form_class = SignUpForm
    model = User
    fields = ['first_name','email','password']
    template_name = 'edit.html'
    template_name_suffix = '_update_form'

    def get_object(self, queryset=None):
        return self.model.objects.get(username=self.request.user)
        # return self.request.GET['pk']
        # return UserInfo.request(pk=self.request.GET.get('pk'))
        # return UserInfo.objects.get(pk=self.request.GET.get('pk'))

# class UserInfoView(LoginRequiredMixin, FormView):
#     form_class = SignUpForm
#     template_name = 'edit.html'
#
#     def get_initial(self):
#         initial = super(UserInfoView, self).get_initial()
#         if self.request.user.additionals.count() > 0:
#             user_info = self.request.user.additionals.all()[0]
#             initial['name'] =
#             initial['password1'] = user_info.use
#             initial['password2'] = user_info.address
#             initial['email'] = user_info.
#         return initial
#
#     def form_valid(self, form):
#         if self.request.user.additionals.count() > 0:
#             user_info = self.request.user.additionals.all()[0]
#             user_info.phone_number = form.data['phone_number']
#             user_info.save()
#         else:
#             user_info = UserInfo()
#             user_info.user = self.request.user
#             user_info.phone_number = form.data['phone_number']
#             user_info.save()
#         return super(UserInfoView, self).form_valid(form)
#
#
# # # TODO: see CreateView later
# # class BetterUserInfoView(LoginRequiredMixin, UpdateView):
# #     model = UserInfo
# #     form_class = SignUpForm
# #     template_name = 'edit'
# #     success_url = '/profile/'
# #
# #     def get_object(self, queryset=None):
# #         if self.request.user.additionals.count() > 0:
# #             return self.request.user.additionals.all()[0]
# #         return None


def cafe_view(request, slug):
    cafe = Cafe.objects.get(id=slug)
    return render(request, 'cafe.html', {'cafe': cafe})


def profile_view(request, slug):
    user = User.objects.get(id=slug)
    return render(request, 'profile.html', {'user': user})

def profile_edit(request, slug):
    user = User.objects.get(id=slug)
    return render(request, 'profile.html', {'user': user})

# class CafeView(DetailView):
#     model = Cafe
#     template_name = 'cafe.html'
#
#     def get_context_data(self, **kwargs):
#         print(kwargs)
#         cafe = Cafe.objects.get(id=kwargs)

        # context = s.get_context_data(**kwargs)
        # return context
    # def get_queryset(self):
    #     self.request.GET['q']
    #     return Cafe.objects.filter('q')
        #  query = Cafe.objects.GET.get('q')
        # if query:
        #     query_list = query.split()
        #     result = result.filter(
        #         reduce(operator.and_,
        #                (Q(title__icontains=q) for q in query_list)) |
        #         reduce(operator.and_,
        #                (Q(content__icontains=q) for q in query_list))
        #     )
        #
        # return result

class LoginView(FormView):
    success_url = '/cafe/index/'
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        if(form.get_user().additionals.first().is_active):
            login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)
#
# class SignupView(FormView):
#     success_url = '/index/'
#     form_class = SignUpForm
#     template_name = 'signup.html'
# def login(request):
#     print("Sasasas")
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         print(form.data)
#         if form.is_valid():
#              username = form.cleaned_data.get('username')
#              raw_password = form.cleaned_data.get('password1')
#              user = authenticate(username=username, password=raw_password)
#              login(request, user)
#              return redirect('cafe/index')
#
#     else:
#         form = SignUpForm()
#         print(form.errors)
#     return render(request, 'registration/login.html', {'form': form})


def signup(request):
    comments_list = User.objects.order_by('-created_at')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.data)
        if form.is_valid():
            user = form.save()
            user_info = User()
            user_info.user = user
            user_info.is_active = True
            user_info.save()
            user.save()
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
                return redirect('/cafe/index')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')


    else:
        form = SignUpForm()
    print(form.errors)
    return render(request, 'signup.html', {'comments': comments_list,'form': form})

