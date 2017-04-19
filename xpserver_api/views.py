from django.http.response import HttpResponse
from xpserver_web.models import Profile
from django.contrib.auth.models import User
from xpserver_api.services import EmailSender


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
