from django.urls import path

from ...controller.registration.login_controller import LoginController
from ....api.controller.registration.register_controller import RegisterController

urlpatterns = [
    path('register/', RegisterController.as_view({'get': 'retrieve'}), name='register'),
    path('register/create/', RegisterController.as_view({'post': 'post'}), name='create_register'),
    path('login/', LoginController.as_view({'post': 'post'}), name='login'),
]
