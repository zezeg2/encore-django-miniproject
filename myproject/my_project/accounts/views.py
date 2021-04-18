from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
# def signup(request):
#     pass
signup = CreateView.as_view(
    form_class = UserCreationForm,
    template_name = 'form.html',
    success_url=settings.LOGIN_URL,

)
# def login(request):
#     pass
login = LoginView.as_view(
    template_name='form.html',
) 


# def logout(request):
#     pass

logout = LogoutView.as_view(
    next_page = settings.LOGIN_URL
)
@login_required
def profile(request):
    return render(request, 'profile.html')