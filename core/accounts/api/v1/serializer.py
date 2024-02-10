from rest_framework import serializers
from ...models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=250,write_only=True)

    class Meta:
        model = User
        fields =['email', 'password','password1']

    def validate(self, attrs):
        # Checking that the password and password1 are equal or not
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError({'detail':'passwords doesnt match'})
        # try to validate the password
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'detail':list(e.messages)})
                    
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1', None)
        # Using the create_user function in the model.py for create user
        return User.objects.create_user(**validated_data)
    



class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email address"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data['email'] = self.user.email
        validated_data['user_id'] = self.user.id
        return validated_data