from django.urls import path

from ....api.controller.reserve.reserve_controller import ReserveController

urlpatterns = [
    path('create/', ReserveController.as_view({'post': 'post'}), name='create_reserve'),
    path('list/', ReserveController.as_view({'get': 'get'}), name='list_of_reservations'),
    path('cancel/', ReserveController.as_view({'patch': 'patch'}), name='cancel_reservations'),
    path('change/', ReserveController.as_view({'patch': 'change_seat'}), name='change_reservations'),

]