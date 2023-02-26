from django.urls import path

from ....api.controller.resell.resell_controller import ResellController

urlpatterns = [
    path('create/', ResellController.as_view({'patch': 'patch'}), name='create_resell'),
]