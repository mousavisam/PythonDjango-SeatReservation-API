from ...enum.seat_enum import SeatStatus, Position
from ...model.room_entity import Room
from ...model.seat_entity import Seat


class SeatLogic:

    def insert_seat(self, count_of_seat, price, position,room:Room):
        seat_number = Seat.objects.count()
        for _ in range(count_of_seat):
            Seat.objects.create(room=room, price=price, status=SeatStatus, position=position, seat_number=seat_number + 1,)

            seat_number +=1

    def calculate_seat_price(self, room_length):
        rows_of_room = room_length * 2
        count_of_seat_per_row = room_length * 2
        rows_with_regular_price = rows_of_room - 4

        seat_info = dict()
        seat_info['count_of_highest_price'] = 1 * rows_of_room
        seat_info['count_of_lowest_price'] = 1 * rows_of_room
        seat_info['count_of_middle_price'] = 2 * rows_of_room
        seat_info['count_of_regular_price'] = rows_with_regular_price * count_of_seat_per_row
        return seat_info, rows_of_room



