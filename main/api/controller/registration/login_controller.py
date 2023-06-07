from rest_framework.request import Request
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from drf_spectacular.utils import extend_schema

from ....api.serializer.Registration.login_serializer import LoginRequest
from ....logic.register.login_logic import LoginLogic


class LoginController(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.login_logic = LoginLogic()

    @extend_schema(
        request=LoginRequest,
        tags=["Auth"],
        responses={201: dict},
    )
    def post(self, request: Request):
        serializer = LoginRequest(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get("username", None)
            password = serializer.validated_data.get("password", None)
            response = self.login_logic.login(username, password)

            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
