from django.urls import path

from ....api.controller.room.room_controller import CreateRoomController

urlpatterns = [
    path('create/', CreateRoomController.as_view({'post': 'post'}), name='create_room'),
]