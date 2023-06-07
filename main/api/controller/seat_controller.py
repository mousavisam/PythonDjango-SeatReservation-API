from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..serializer.seat.seat_serializer import SeatSerializer
from ...enum.seat_enum import SeatStatus
from ...logic.seat.seat_logic import SeatLogic

from drf_spectacular.utils import extend_schema


class SeatController(ViewSet):

    def __init__(self):
        super().__init__()
        self.seat_logic = SeatLogic()

    @extend_schema(
        tags=["Room"],
        responses={200: SeatSerializer},
    )
    def get(self, request: Request):
        try:
            list_of_unreserved_seats = self.seat_logic.get_seats_by_status(seat_status=SeatStatus.UNRESERVED)
            serialized_response = SeatSerializer(list_of_unreserved_seats, many=True)
            return Response(data=serialized_response.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)

