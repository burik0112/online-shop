from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


def password_change_done(request):
    messages.add_message(request, messages.INFO, 'Password changed successfully')
    return redirect(reverse('profile:home'))
