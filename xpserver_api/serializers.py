from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from xpserver_api.permissions import IsCreationOrIsAuthenticated
from xpserver_api.services import generate_activation_code, EmailSender
from xpserver_web.models import Profile
from rest_framework.exceptions import APIException


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email')

    def create(self, validated_data):
        email = validated_data['email']
        if email:
            user = User.objects.create(**validated_data)
            user.username = email
            user.is_active = False
            user.save()
            profile = Profile.objects.create(user=user, activation_code=generate_activation_code())
            profile.save()
            email_sender = EmailSender()
            email_sender.send_activation_email_with(profile=profile)
            return user
        else:
            raise APIException("Enter a valid email address.")


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCreationOrIsAuthenticated]
