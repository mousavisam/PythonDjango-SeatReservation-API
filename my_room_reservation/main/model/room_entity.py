from django.db import models

from ..enum.room_type import RoomType
from ..model.user_entity import User


class Room(models.Model):
    length = models.PositiveIntegerField()
    count_of_seat = models.PositiveIntegerField()
    count_of_rows = models.PositiveIntegerField()
    type = models.CharField(max_length=20, choices=RoomType.choices)
    business_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    


