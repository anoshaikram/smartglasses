from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from .models import GlassesLocation

# Signup serializer
class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "address", "phone_number", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["email"],  # use email as username
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            email=validated_data["email"],
            address=validated_data.get("address", ""),
            phone_number=validated_data.get("phone_number", ""),
            password=validated_data["password"]
        )
        return user


# Login serializer
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        return user


#locationSerializer
class GlassesLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlassesLocation
        fields = ['id', 'glasses_id', 'latitude', 'longitude', 'timestamp']
