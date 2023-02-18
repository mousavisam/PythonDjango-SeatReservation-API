from rest_framework import status
from rest_framework.viewsets import ViewSet

from ...serializer.Registration.register_serializer import UserSerializer
from ....logic.register.register_logic import RegisterLogic
from rest_framework.response import Response


class RegisterController(ViewSet):

    def __init__(self):
        self.register_logic = RegisterLogic

    def retrieve(self, request):
        users = self.register_logic.get_all_users()

        serialized_response = UserSerializer(users)
        return Response(data=serialized_response.data, status=status.HTTP_200_OK)
