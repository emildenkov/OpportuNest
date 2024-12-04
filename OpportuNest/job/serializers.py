from rest_framework import serializers
from OpportuNest.accounts.serializers import AppUserSerializer
from OpportuNest.job.models import Job


class JobSerializer(serializers.ModelSerializer):
    posted_by = AppUserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'