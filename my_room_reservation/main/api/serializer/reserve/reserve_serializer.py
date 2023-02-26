from rest_framework import serializers

from ....model.reservation_entity import Reservation
from ....model.seat_entity import Seat


class ReserveSerializer(serializers.Serializer):
    seat_number = serializers.IntegerField(min_value=1, required=True)
    room_id = serializers.IntegerField(min_value=1, required=True)
    price = serializers.DecimalField(required=True, min_value=0.1, max_digits=9, decimal_places=3)


class ReservesListSerializer(serializers.ModelSerializer):
    seat_number = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['id', 'final_price', 'seat_number', 'status', 'creation_time']

    def get_seat_number(self, obj):
        return obj.seat.number


class UpdateReserveSerializer(serializers.Serializer):
    reservation_id = serializers.IntegerField(min_value=1, required=True)


class ChangeSeatSerializer(serializers.ModelSerializer):
    former_reservation_id = serializers.IntegerField(min_value=1, required=True)
    room_id = serializers.IntegerField(min_value=1, required=True)

    class Meta:
        model = Seat
        fields = ['number', 'price', 'room_id', 'former_reservation_id']