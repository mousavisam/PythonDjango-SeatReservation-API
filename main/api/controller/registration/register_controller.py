from urllib.request import Request

from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from ...serializer.Registration.register_serializer import UserSerializer, UserRegisterSerializer
from ....logic.register.register_logic import RegisterLogic


class RegisterController(ViewSet):
    permission_classes = [AllowAny]

    def __init__(self):
        super().__init__()
        self.register_logic = RegisterLogic()

    @extend_schema(
        tags=["Auth"],
        responses={200: UserSerializer},
    )
    def retrieve(self, request: Request):
        users = self.register_logic.get_all_users()

        serialized_response = UserSerializer(users, many=True)
        return Response(data=serialized_response.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=UserRegisterSerializer,
        tags=["Auth"],
        responses={200: dict}
    )
    def post(self, request: Request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                username = serializer.validated_data.get('username')
                password = serializer.validated_data.get('password')
                email = serializer.validated_data.get('email')
                first_name = serializer.validated_data.get('first_name')
                last_name = serializer.validated_data.get('last_name')
                user_type = serializer.validated_data.get('type')
                self.register_logic.register_new_user(username=username, password=password,
                                                      email=email, first_name=first_name,
                                                      last_name=last_name, type=user_type)
                return Response(data="", status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
