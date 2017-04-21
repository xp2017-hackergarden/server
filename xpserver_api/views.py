from django.http.response import HttpResponse
from xpserver_web.models import Profile
from django.contrib.auth.models import User
from xpserver_api.services import EmailSender
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.authtoken.models import Token


def activate_account(request):
    response = ''
    if request.method == "GET":
        activation_code = request.GET.get('activation_code')
        user_name = request.GET.get('user_name')

        if activation_code and user_name:
            try:
                profile = Profile.objects.get(user__username=user_name, activation_code=activation_code)

                if not profile.user.is_active:
                    profile.user.is_active = True
                    password = User.objects.make_random_password()
                    profile.user.set_password(password)
                    profile.user.save()
                    profile.save()
                    email_sender = EmailSender()
                    email_sender.send_password_email_for(profile.user.email, password)
                    response = "Account activated"
                else:
                    response = "Account already activated"

            except Profile.DoesNotExist:
                response = "Invalid user or activation code"

        else:
            response = 'Missing parameters'
    return HttpResponse(response)


def response_json_with_status_code(status_code, response):
    return JsonResponse(status=status_code, data={'response': response})


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def obtain_token(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=username)

        if user.check_password(password):
            response = str(Token.objects.get(user=user))
            status_code = 202
        else:
            response = "Wrong password"
            status_code = 401

    except User.DoesNotExist:
        response = "User does not exist"
        status_code = 404
    except Token.DoesNotExist:
        response = "User does not have a token"
        status_code = 404
    finally:
        return response_json_with_status_code(status_code, response)
