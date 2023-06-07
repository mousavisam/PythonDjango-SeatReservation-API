from rest_framework import serializers

from ....model.user_entity import User
from ....shared.utils import RoomReservationUtils


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(validators=[RoomReservationUtils.validate_username])
    password = serializers.CharField(validators=[RoomReservationUtils.validate_password])

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'type']
