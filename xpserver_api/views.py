from django.http.response import HttpResponse
from xpserver_web.models import Profile
from django.contrib.auth.models import User
from xpserver_api.services import EmailSender
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.authtoken.models import Token


def response_json_with_status_code(status_code, response):
    return JsonResponse(status=status_code, data={'response': response})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def activate_account(request):
    response = "Error occurred"
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


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def activate_mobile_app(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    fcm_registration_id = request.POST.get('fcm_registration_id')
    response = "Error occurred"
    status_code = 500

    try:
        user = User.objects.get(username=username)

        if user.check_password(password):

            try:
                profile = Profile.objects.get(user=user)
                profile.fcm_registration_id = fcm_registration_id
                profile.save()
                response = str(Token.objects.get(user=user))
                status_code = 202
            except:
                response = "Could not activate the app"
                status_code = 404
        else:
            response = "Wrong password"
            status_code = 401

    except User.DoesNotExist:
        response = "User does not exist"
        status_code = 404
    except Token.DoesNotExist:
        response = "Could not activate the app"
        status_code = 404
    finally:
        return response_json_with_status_code(status_code, response)
