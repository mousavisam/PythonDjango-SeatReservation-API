from rest_framework import serializers


class NotifSerializer(serializers.Serializer):
    notification_id = serializers.IntegerField(min_value=1, required=True)