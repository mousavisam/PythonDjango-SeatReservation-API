from django.urls import path

from ....api.controller.seat_controller import SeatController

urlpatterns = [
    path('list/', SeatController.as_view({'get': 'get'}), name='list_of_seats'),
]

