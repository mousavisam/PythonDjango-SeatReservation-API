import datetime
from decimal import Decimal
from typing import Union

from ..account.account_logic import AccountLogic
from ..notif.notification_logic import NotificationLogic
from ..seat.seat_logic import SeatLogic
from ..transaction.transaction_logic import TransactionLogic
from ...enum.notification_type import NotificationType
from ...enum.reservation_status import ReservationStatus
from ...enum.seat_enum import SeatStatus
from ...enum.transaction_status import TransactionStatus, TransactionType
from ...model.reservation_entity import Reservation
from ...model.seat_entity import Seat
from ...model.user_entity import User


class ReserveLogic:

    def __init__(self):
        self.seat_logic = SeatLogic()
        self.notif_logic = NotificationLogic()
        self.account_logic = AccountLogic()
        self.transaction_logic = TransactionLogic()

    def insert_reserve(self, reserver: User, final_price: Decimal, seat: Seat,
                       business_owner: User, status: ReservationStatus):
        return Reservation.objects.create(reserver=reserver, final_price=final_price, seat=seat,
                                          seat_owner=business_owner,
                                          status=status)

    def update_reserve_status(self, reserve: Reservation, status: ReservationStatus):
        reserve.status = status
        try:
            reserve.save()
            return True
        except Exception:
            return False

    def update_accounts_and_insert_transactions(self, price, seat, user, reserve, owner_account):
        self.account_logic.update_account_balance(user.account.first(), balance=-price)
        self.transaction_logic.insert_transaction(account=user.account.first(),
                                                  amount=-price,
                                                  status=TransactionStatus.SUCCESS,
                                                  type=TransactionType.RESERVE, reservation=reserve,
                                                  seat_owner_account=seat.room.business_owner.account.first(),
                                                  description="reserve created")
        self.account_logic.update_account_balance(owner_account, balance=price)
        self.transaction_logic.insert_transaction(account=owner_account,
                                                  amount=price,
                                                  status=TransactionStatus.SUCCESS,
                                                  type=TransactionType.RESERVE, reservation=reserve,
                                                  seat_owner_account=seat.room.business_owner.account.first(),
                                                  description=f"some one with id {user.id} reserved one seat")

    def make_reservation(self, seat_number, room_id, price, user):
        formal_reserve = None
        seat = self.seat_logic.get_seat_by_seat_number_and_room_id(seat_numer=seat_number, room_id=room_id)
        owner = seat.room.business_owner
        owner_account = seat.room.business_owner.account.first()
        if seat.status == SeatStatus.RESELL:
            formal_reserve = self.get_reserve_by_seat(seat)
            owner = formal_reserve.reserver
            owner_account = owner.account.first()

        if seat.status != SeatStatus.RESERVED:
            reserve = self.insert_reserve(reserver=user, final_price=price, seat=seat,
                                          business_owner=owner,
                                          status=ReservationStatus.REQUESTED)

            self.update_accounts_and_insert_transactions(price, seat, user, reserve, owner_account=owner_account)

            if self.update_reserve_status(reserve, status=ReservationStatus.SUCCESS):
                if seat.status == SeatStatus.RESELL:
                    self.update_reserve_status(formal_reserve, ReservationStatus.CANCELED)

                    self.notif_logic.insert_notif(user=formal_reserve.reserver,
                                                  message=f"your resell with id {formal_reserve.id} has been reserved again",
                                                  type=NotificationType.PRIVATE, creation_time=datetime.datetime.now())

                self.seat_logic.update_seat_status(seat, status=SeatStatus.RESERVED)
                self.notif_logic.insert_notif(
                    message=f"your reservation with id {reserve.id} has been created successfully",
                    type=NotificationType.PRIVATE, creation_time=datetime.datetime.now())
                return {'response': 'your seat reserved successfully'}

            else:
                return {'response': 'your reservation failed'}
        else:
            return {'response': 'This seat is already reserved'}

    def get_reservations_by_reserver(self, reserver: User):
        return Reservation.objects.filter(reserver=reserver)

    def get_reserve_by_id(self, reserve_id: int) -> Reservation:
        return Reservation.objects.filter(id=reserve_id).first()

    def get_reserve_by_seat(self, seat: Seat) -> Reservation:
        return Reservation.objects.filter(seat=seat).first()

    def make_reserve_cancel(self, reserve_id: int, user: User, change_seat=False) -> Union[str, Exception]:
        reserve = self.get_reserve_by_id(reserve_id=reserve_id)
        try:
            cancel_rate = 0 if change_seat else Decimal(0.2) * reserve.final_price
            self.update_reserve_status(reserve=reserve, status=ReservationStatus.CANCELED)
            self.account_logic.update_account_balance(user.account.first(), balance=reserve.final_price - cancel_rate)
            self.transaction_logic.insert_transaction(account=user.account.first(),
                                                      amount=reserve.final_price - cancel_rate,
                                                      status=TransactionStatus.SUCCESS, type=TransactionType.CANCELED,
                                                      description="reserve canceled")
            return "reserve canceled"

        except Exception as e:
            return e

    def change_seat(self, former_reservation_id, seat_number, price, room_id, user):
        try:
            self.make_reserve_cancel(reserve_id=former_reservation_id, user=user, change_seat=True)
            self.make_reservation(seat_number=seat_number, price=price, room_id=room_id, user=user)
            return "your seat changed with the new one"

        except Exception as e:
            raise e