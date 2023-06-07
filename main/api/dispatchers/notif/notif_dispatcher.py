from django.urls import path

from ....api.controller.notif.notif_controller import NotifController

urlpatterns = [
    path('close/', NotifController.as_view({'patch': 'close_notif'}), name='close_notif'),
]