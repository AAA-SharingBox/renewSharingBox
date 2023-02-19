from django.contrib.auth.views import LoginView, LogoutView
from .forms import MyUserCreationForm, LoginForm
from django.views.generic import CreateView
from django.urls import path

urlpatterns = [
    
    path('signup/', CreateView.as_view(
        template_name='account/signup.html',
        form_class=MyUserCreationForm,
        success_url='/'
    ), name='signup'),

    path('login/', LoginView.as_view(
        redirect_authenticated_user = True,
        form_class = LoginForm,
        template_name = 'account/login.html',
    ), name = 'login'),

    path('logout/', LogoutView.as_view(), name = 'logout'),

]