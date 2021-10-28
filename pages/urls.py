from django.contrib.auth.views import LoginView
from django.urls import path

from pages.views import ContactCreateView, HomeView, AboutView

app_name = 'pages'

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', AboutView.as_view(), name='register'),
    path('', HomeView.as_view(), name='home'),
]
