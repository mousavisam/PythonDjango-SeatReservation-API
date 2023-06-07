from rest_framework import serializers


class ResellSerializer(serializers.Serializer):
    reservation_id = serializers.IntegerField(min_value=1, required=True)
    new_price = serializers.DecimalField(max_digits=12, decimal_places=3, min_value=0.1, required=False)