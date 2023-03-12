from django.contrib import messages
from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views

from WeatherApp.accounts.forms import UserCreateForm

# Create your views here.
UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'

    def form_invalid(self, form):
        messages.error(self.request, "Username and/or password is incorrect!")
        return super().form_invalid(form)


class RegistrationView(views.CreateView):
    template_name = 'accounts/registration-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    success_message = "User is sign up successfully!"

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def form_invalid(self, form):
        if form['password1'].value() != form['password2'].value():
            messages.error(self.request, "Passwords doesn't match")
        else:
            messages.error(self.request, "Username exist!!")
        return super().form_invalid(form)


class UserDetailsView(views.DetailView):
    template_name = 'accounts/user-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/user-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'picture')
    success_message = "User was updated successfully"


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/user-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('login')
    success_message = "User was deleted successfully"


class SignOut(auth_views.LogoutView):
    next_page = reverse_lazy('login')
