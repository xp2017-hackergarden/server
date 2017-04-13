from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def main(request):
    return render(request, 'base.html')


def register(request):
    return render(request, 'registration/registration.html')


def ping(request):
    return HttpResponse("I am alive.", content_type="text/plain")
