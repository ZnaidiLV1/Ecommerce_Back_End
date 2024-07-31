from rest_framework import serializers
from .models import CustomUser


class userserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password', None)  # Extract password
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)  # Set password securely
        instance.save()
        return instance
