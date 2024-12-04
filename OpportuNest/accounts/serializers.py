from rest_framework import serializers
from OpportuNest.accounts.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'email']