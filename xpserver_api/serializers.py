from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from xpserver_api.services import generate_activation_code, EmailSender
from xpserver_web.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'email')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        email = validated_data['email']
        user.username = email
        user.is_active = False
        user.save()
        profile = Profile.objects.create(user=user, activation_code=generate_activation_code())
        profile.save()
        email_sender = EmailSender()
        email_sender.send_activation_email_with(profile=profile)
        return user


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
