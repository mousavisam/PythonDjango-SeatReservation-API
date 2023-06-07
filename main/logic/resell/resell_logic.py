import datetime

from ..notif.notification_logic import NotificationLogic
from ..seat.seat_logic import SeatLogic
from ...enum.notification_type import NotificationType
from ...enum.reservation_status import ReservationStatus
from ...enum.seat_enum import SeatStatus
from ...logic.reserve.reserve_logic import ReserveLogic
from ...model.resell_entity import Resell


class ResellLogic:

    def __init__(self):
        self.reserve_logic = ReserveLogic()
        self.seat_logic = SeatLogic()
        self.notif_logic = NotificationLogic()

    def insert_resell(self, **kwargs):
        Resell.objects.create(**kwargs)

    def make_reserve_resell(self, reserve_id, user, new_price):
        try:
            reserve = self.reserve_logic.get_reserve_by_id(reserve_id=reserve_id)
            if not new_price or new_price > reserve.final_price:
                new_price = reserve.final_price

            self.reserve_logic.update_reserve_status(reserve, status=ReservationStatus.RESELL)
            self.insert_resell(reserver=user, reservation=reserve, new_price=new_price)
            self.seat_logic.update_seat_status(reserve.seat, status=SeatStatus.RESELL)
            self.notif_logic.insert_notif(message=f"status of seat {reserve.seat.number} is changed to unreserved",
                                          type=NotificationType.PUBLIC, creation_time=datetime.datetime.now())
            return "your reserve status changed to resell successfully"

        except Exception as e:
            return e

    def get_all_resells(self):
        return Resell.objects.all()

    def get_all_reservable_seats(self):
        reservable_seats = self.seat_logic.get_seats_by_status(seat_status=SeatStatus.UNRESERVED)
        resell_seats = self.get_all_resells()
        result = list()
        for index, resell_seat in enumerate(resell_seats):
            result.append(dict())
            result[index]['price'] = resell_seat.reservation.final_price
            result[index]['discount_ratio'] = resell_seat.discount_ratio
            result[index]['position'] = resell_seat.reservation.seat.position
            result[index]['business_owner'] = resell_seat.reservation.seat.room.business_owner.username
            result[index]['status'] = resell_seat.reservation.seat.status
            result[index]['room'] = resell_seat.reservation.seat.room.id

        return result, reservable_seats