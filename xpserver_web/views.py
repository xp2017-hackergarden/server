from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .forms import RegisterForm


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
            # TODO Implement activation via email here.
            user.save()
            return redirect("/")
        else:
            return render(request, 'registration/register.html', {'registration_form': registration_form})

    elif request.method == "GET":
        registration_form = RegisterForm()
        return render(request, 'registration/register.html', {'registration_form': registration_form})


def ping(request):
    return HttpResponse("I am alive.", content_type="text/plain")
