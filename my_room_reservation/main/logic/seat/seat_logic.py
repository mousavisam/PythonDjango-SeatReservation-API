import datetime
from decimal import Decimal

from django.db.models import QuerySet

from ..notif.notification_logic import NotificationLogic
from ...enum.notification_type import NotificationType
from ...enum.seat_enum import SeatStatus
from ...model.room_entity import Room
from ...model.seat_entity import Seat


class SeatLogic:

    def __init__(self):
        self.notif_logic = NotificationLogic()

    def insert_seat(self, count_of_seat, price, position, room: Room):
        seat_number = Seat.objects.count()
        for _ in range(count_of_seat):
            seat = Seat.objects.get_or_create(room=room, price=price, status=SeatStatus.UNRESERVED, position=position,
                                              number=seat_number + 1)
            self.notif_logic.insert_notif(message=f"this seat with number {seat[0].number} added to sell list",
                                          type=NotificationType.PUBLIC, creation_time=datetime.datetime.now())

            seat_number += 1

    def calculate_seat_price(self, length):
        rows_of_room = length * 2
        count_of_seat_per_row = length * 2

        rows_with_regular_price = rows_of_room - 4

        seat_info = dict()
        seat_info['count_of_highest_price'] = 1 * rows_of_room
        seat_info['count_of_lowest_price'] = 1 * rows_of_room
        seat_info['count_of_middle_price'] = 2 * rows_of_room
        seat_info['count_of_regular_price'] = rows_with_regular_price * count_of_seat_per_row
        return seat_info, rows_of_room

    def get_seats_by_status(self, seat_status: SeatStatus) -> QuerySet:
        return Seat.objects.filter(status=seat_status)

    def get_reservable_seats(self):
        return Seat.objects.exclude(status=SeatStatus.RESERVED)

    def get_seat_by_seat_number_and_room_id(self, seat_numer: int, room_id: int) -> Seat:
        return Seat.objects.filter(number=seat_numer, room__id=room_id).first()

    def update_seat_price(self, seat: Seat, new_price: Decimal):
        seat.price = new_price
        try:
            seat.save()
            return True
        except Exception:
            return False

    def update_seat_status(self, seat: Seat, status: SeatStatus):
        seat.status = status
        try:
            seat.save()
            return True
        except Exception:
            return False
