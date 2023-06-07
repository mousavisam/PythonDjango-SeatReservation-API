from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ....api.serializer.notif.notif_serializer import NotifSerializer
from ....logic.notif.notification_logic import NotificationLogic


class NotifController(ViewSet):

    def __init__(self):
        super().__init__()
        self.notif_logic = NotificationLogic()

    @extend_schema(
        parameters=[NotifSerializer],
        tags=["Notif"],
        responses={200: str},
    )
    def close_notif(self, request: Request):
        notif_serializer = NotifSerializer(data=request.query_params)
        if notif_serializer.is_valid():
            try:
                notif_id = notif_serializer.validated_data.get('notification_id')
                self.notif_logic.close_notif(notif_id)
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                return Response(data=str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)

        else:
            return Response(notif_serializer.errors, status=status.HTTP_400_BAD_REQUEST)