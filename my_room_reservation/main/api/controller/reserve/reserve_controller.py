from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ....api.serializer.reserve.reserve_serializer import ReserveSerializer, ReservesListSerializer, \
    UpdateReserveSerializer, ChangeSeatSerializer
from ....logic.reserve.reserve_logic import ReserveLogic


class ReserveController(ViewSet):

    def __init__(self):
        super().__init__()
        self.reserve_logic = ReserveLogic()

    @extend_schema(
        request=ReserveSerializer,
        tags=["Reservation"],
        responses={201: str},
    )
    def post(self, request: Request):
        reserve_serializer = ReserveSerializer(data=request.data)
        if reserve_serializer.is_valid():
            try:
                seat_number = reserve_serializer.validated_data.get("seat_number")
                price = reserve_serializer.validated_data.get("price")
                room_id = reserve_serializer.validated_data.get("room_id")
                response = self.reserve_logic.make_reservation(seat_number, room_id, price, user=request.user)

                return Response(data=response['response'], status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(str(e), status=status.HTTP_503_SERVICE_UNAVAILABLE)

        else:
            return Response(reserve_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Reservation"],
        responses={200: ReservesListSerializer},
    )
    def get(self, request: Request):
        try:
            reservations_list = self.reserve_logic.get_reservations_by_reserver(reserver=request.user)
            serialized_data = ReservesListSerializer(reservations_list, many=True)
            return Response(data=serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[UpdateReserveSerializer],
        tags=["Reservation"],
        responses={200: str},
    )
    def patch(self, request: Request):
        reserve_serializer = UpdateReserveSerializer(data=request.query_params)
        if reserve_serializer.is_valid():
            try:
                reserve_id = reserve_serializer.validated_data.get("reservation_id")
                response = self.reserve_logic.make_reserve_cancel(reserve_id, user=request.user)
                if isinstance(response, str):
                    return Response(data=response, status=status.HTTP_200_OK)
                else:
                    return Response(data=str(response), status=status.HTTP_503_SERVICE_UNAVAILABLE)

            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[ChangeSeatSerializer],
        tags=["Reservation"],
        responses={200: str},
    )
    def change_seat(self, request: Request):
        change_seat_serializer = ChangeSeatSerializer(data=request.query_params)
        if change_seat_serializer.is_valid():
            try:
                former_reservation_id = change_seat_serializer.validated_data.get("former_reservation_id")
                seat_number = change_seat_serializer.validated_data.get("number")
                price = change_seat_serializer.validated_data.get("price")
                room_id = change_seat_serializer.validated_data.get("room_id")
                response = self.reserve_logic.change_seat(former_reservation_id, seat_number, price, room_id,
                                                          request.user)

                return Response(data=response, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
