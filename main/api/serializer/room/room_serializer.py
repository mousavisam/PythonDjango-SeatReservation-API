from rest_framework import serializers

from ....enum.room_type import RoomType


class RegisterRoomSerializer(serializers.Serializer):
    room_length = serializers.IntegerField(min_value=2, required=True)  # A length of room at least should be more than or equal to 2
    regular_seat_price = serializers.FloatField(min_value=1, required=True)
    room_type = serializers.ChoiceField(choices=RoomType.choices, required=True)