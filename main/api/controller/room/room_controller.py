from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ....api.serializer.room.room_serializer import RegisterRoomSerializer
from ....logic.room.room_logic import RoomLogic


class CreateRoomController(ViewSet):

    permission_classes = [IsAuthenticated]

    def __init__(self):
        super().__init__()
        self.room_logic = RoomLogic()

    @extend_schema(
        request=RegisterRoomSerializer,
        tags=["Room"],
        responses={201: str},
    )
    def post(self, request: Request):
        serializer = RegisterRoomSerializer(data=request.data)
        if serializer.is_valid():
            try:
                room_length = serializer.validated_data.get('room_length')
                regular_seat_price = serializer.validated_data.get('regular_seat_price')
                room_type = serializer.validated_data.get("room_type")
                result = self.room_logic.calculate_and_add_seats(user_id=request.user.id, room_type=room_type,
                                                                 room_length=room_length,
                                                                 regular_seat_price=regular_seat_price)

                return Response(data=result, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
