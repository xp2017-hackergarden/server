from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import RegisterForm
from xpserver_web.models import Profile
from xpserver_api.services import generate_activation_code, EmailSender
from django.contrib import messages


@login_required
def main(request):
    return render(request, 'base.html')


def username_present(username):
    return User.objects.filter(username=username).exists()


def register(request):
    if request.method == "POST":
        registration_form = RegisterForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.username = user.email
            user.is_active = False
            user.save()
            profile = Profile.objects.create(user=user, activation_code=generate_activation_code())
            profile.save()
            email_sender = EmailSender()
            email_sender.send_activation_email_with(profile=profile)
            messages.add_message(request, messages.INFO,
                                 'Successfully registered. Please check your email for validation link.')
            return redirect("/")
        else:
            return render(request, 'registration/register.html', {'registration_form': registration_form})

    elif request.method == "GET":
        registration_form = RegisterForm()
        return render(request, 'registration/register.html', {'registration_form': registration_form})


def ping(request):
    return HttpResponse("I am alive.", content_type="text/plain")
