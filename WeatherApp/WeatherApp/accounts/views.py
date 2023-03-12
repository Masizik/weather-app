from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class RegistrationView(views.CreateView):
    template_name = 'accounts/registration-page.html'


class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-detail-page.html'


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit-page.html'


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete-page.html'


class SignOut(auth_views.LogoutView):
    next_page = reverse_lazy('login')
