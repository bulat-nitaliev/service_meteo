from rest_framework import serializers
from meteo.models import User, City



class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
          "username",
          "password",
          "email",
          "first_name",
          "last_name",
        )
    def create(self, validated_data):
        user = User.objects.create(
          username=validated_data['username'],
          email=validated_data['email'],
          first_name=validated_data['first_name'],
          last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'