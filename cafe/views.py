from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.edit import FormView
from cafe.forms.user_forms import SignUpForm
from cafe.models import UserInfo, Cafe
import json
import urllib
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

# from .models import Comment
# from .forms import CommentForm

from django.views.generic.list import ListView

class HomePageView(ListView):
    model = Cafe
    template_name = 'index.html'

class LoginView(FormView):
    success_url = '/login/'
    form_class = AuthenticationForm
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)
#
# class SignupView(FormView):
#     success_url = '/index/'
#     form_class = SignUpForm
#     template_name = 'signup.html'


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return redirect('http://127.0.0.1:8000/cafe/index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



    # def form_valid(self, form):
        # if self.request.user.additionals.count() > 0:
        #     user_info = self.request.user.additionals.all()[0]
        #     user_info.username = form.data['username']
        #     user_info.save()
        # else:
        #     user_info = UserInfo()
        #     user_info.user = self.request.user
        #     user_info.username = form.data['username']
        #     user_info.save()
        # return super(UserInfoView, self).form_valid(form)
from django.core.mail import send_mail

# if form.is_valid():
#     subject = form.cleaned_data['subject']
#     message = form.cleaned_data['message']
#     sender = form.cleaned_data['sender']
#     cc_myself = form.cleaned_data['cc_myself']
#
#     recipients = ['info@example.com']
#     if cc_myself:
#         recipients.append(sender)
#
#     send_mail(subject, message, sender, recipients)
#     return HttpResponseRedirect('/thanks/')

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})
def comments(request):
    comments_list = UserInfo.objects.order_by('-created_at')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

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
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('comments')
    else:
        form = SignUpForm()

    return render(request, 'index.html', {'comments': comments_list, 'form': form})
