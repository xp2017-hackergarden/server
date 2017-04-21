from django.core import exceptions
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm
from xpserver_web.models import Profile
from xpserver_api.services import generate_activation_code, EmailSender


@login_required
def main(request):
    return render(request, 'base.html')


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
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully registered. Please check your email for validation link.')
            return redirect("/")
        else:
            return render(request, 'registration/register.html', {'registration_form': registration_form})

    elif request.method == "GET":
        registration_form = RegisterForm()
        return render(request, 'registration/register.html', {'registration_form': registration_form})


@login_required
def change_password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        repeated = request.POST.get('repeated_password')
        errors = dict()
        if password != repeated:
            messages.add_message(request, messages.ERROR,
                                 "You didn't repeat password correctly.")
            return render(request, 'registration/changePassword.html',
                          {'password': password, 'repeated_password': repeated})
        else:
            try:
                password_validation.validate_password(password)
            except exceptions.ValidationError as e:
                errors['password'] = list(e.messages)
                for error in errors['password']:
                    messages.add_message(request, messages.ERROR, error)
                return render(request, 'registration/changePassword.html',
                              {'password': password, 'repeated_password': repeated})
            u = User.objects.get(id=request.user.id)
            u.set_password(password)
            u.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Successfully changed password.')
            return redirect("/")
    elif request.method == "GET":
        return render(request, 'registration/changePassword.html')


def ping(request):
    return HttpResponse("I am alive.", content_type="text/plain")
