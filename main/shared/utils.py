import datetime
import re

from rest_framework import serializers


class RoomReservationUtils:

    @staticmethod
    def validate_password(password):
        if len(password) < 5:
            raise serializers.ValidationError("Make sure the length of your password is more than 5 characters")
        elif re.search('[A-Z]', password) is None:
            raise serializers.ValidationError("Make sure your password has a capital letter in it")

    @staticmethod
    def validate_username(username):
        if username.isnumeric():
            raise serializers.ValidationError("username must have characters too!")

    @staticmethod
    def convert_datetime_to_str(datetime_obj: datetime) -> str:
        return datetime_obj.strftime("%Y/%m/%dT%H:%M:%S")
