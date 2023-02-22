import datetime

from ..notif.notification_logic import NotificationLogic
from ..seat.seat_logic import SeatLogic
from ..user.user_logic import UserLogic
from ...enum.notification_type import NotificationType
from ...enum.room_type import RoomType
from ...enum.seat_enum import Position
from ...model.room_entity import Room


class RoomLogic:

    def __init__(self):
        self.user_logic = UserLogic()
        self.seat_logic = SeatLogic()
        self.notif_logic = NotificationLogic()

    def create_room(self, **kwargs):
        return Room.objects.create(**kwargs)

    @classmethod
    def calculate_price_based_on_regular_price(cls, regular_seat_price):
        highest_price = 2 * regular_seat_price
        lowest_price = 0.75 * regular_seat_price
        middle_price = 1.25 * regular_seat_price

        return highest_price, lowest_price, middle_price

    def calculate_and_add_seats(self, user_id, room_length, regular_seat_price, room_type) -> str:
        business_owner = self.user_logic.get_user_by_id(user_id)

        seat_info, rows_of_room = self.seat_logic.calculate_seat_price(room_length=room_length)

        room = self.create_room(count_of_rows=rows_of_room, count_of_seats=rows_of_room**2, business_owner=business_owner, length=room_length, type=RoomType(room_type))

        highest_price, lowest_price, middle_price = self.calculate_price_based_on_regular_price(regular_seat_price=regular_seat_price)

        self.seat_logic.insert_seat(count_of_seat=seat_info['count_of_highest_price'], price=highest_price,
                                    position=Position.FIRST_ROW, room=room)
        self.seat_logic.insert_seat(count_of_seat=seat_info['count_of_lowest_price'], price=lowest_price,
                                    position=Position.LAST_ROW, room=room)
        self.seat_logic.insert_seat(count_of_seat=seat_info['count_of_middle_price'], price=middle_price,
                                    position=Position.MIDDLE_ROWS, room=room)
        self.seat_logic.insert_seat(count_of_seat=seat_info['count_of_regular_price'], price=regular_seat_price,
                                    position=Position.REGULAR_ROWS, room=room)

        self.notif_logic.insert_notif(message=f"{sum(seat_info.values())} seats with different price added",
                                       type=NotificationType.PUBLIC, creation_time=datetime.datetime.now())

        return f"Your room with {sum(seat_info.values())} seats added"










