from rest_framework import serializers 
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'mobileNo', 'password', 'address']
        extra_kwargs = {'password': {'required': True,
                                  'allow_blank': False}}

    def validate(self, data):
        pattern = re.compile("^([0]|\+91)?[6-9]\d{9}$")
        if not pattern.match(data['mobileNo']):
            raise serializers.ValidationError({"mobileNo": "Invalid mobile number."})
        return data