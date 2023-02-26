from rest_framework import serializers

from ....shared.utils import RoomReservationUtils


class LoginRequest(serializers.Serializer):

    username = serializers.CharField(validators=[RoomReservationUtils.validate_username], required=True)
    password = serializers.CharField(validators=[RoomReservationUtils.validate_password], required=True)


