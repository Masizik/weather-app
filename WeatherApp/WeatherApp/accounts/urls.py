from django.urls import path, include

from WeatherApp.accounts.views import SignInView, RegistrationView, UserDetailsView, UserEditView, UserDeleteView, \
    SignOut

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', SignOut.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', UserDetailsView.as_view(), name='user details'),
        path('edit/', UserEditView.as_view(), name='user edit'),
        path('delete/', UserDeleteView.as_view(), name='user delete'),
    ]))

]