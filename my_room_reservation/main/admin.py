from django.contrib import admin

from .model.notification_entity import Notification
from .model.resell_entity import Resell
from .model.reservation_entity import Reservation
from .model.room_entity import Room
from .model.seat_entity import Seat
from .model.transaction_entity import Transaction
from .model.user_entity import User
from .model.account_entity import Account


# Register your models here.
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Notification)
admin.site.register(Resell)
admin.site.register(Reservation)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Transaction)
