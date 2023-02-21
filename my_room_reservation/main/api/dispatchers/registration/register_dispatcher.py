from django.urls import path

from ....api.controller.registration.register_controller import RegisterController

urlpatterns = [
    path('register/', RegisterController.as_view({'get': 'retrieve'}), name='register'),
]
