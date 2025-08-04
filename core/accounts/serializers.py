from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
User = get_user_model()
# ======================================================================================================================
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password], write_only=True)
    confirm_password = serializers.CharField(validators=[validate_password], write_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'password','confirm_password')

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'confirm_password': 'رمزهای عبور مطابقت ندارند'})
        return data

    def create(self, validated_data):
        user=User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

# ======================================================================================================================