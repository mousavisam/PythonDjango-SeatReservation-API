from rest_framework import serializers

from ....model.seat_entity import Seat


class SeatSerializer(serializers.ModelSerializer):
    business_owner = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ['price', 'position', 'status', 'business_owner', 'room', 'number']

    def get_business_owner(self, obj):
        return obj.room.business_owner.username
