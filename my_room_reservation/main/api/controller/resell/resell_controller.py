from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ....api.serializer.resell.resell_serializer import ResellSerializer
from ....logic.resell.resell_logic import ResellLogic


class ResellController(ViewSet):

    def __init__(self):
        super().__init__()
        self.resell_logic = ResellLogic()

    @extend_schema(
        parameters=[ResellSerializer],
        tags=["Resell"],
        responses={200: str},
    )
    def patch(self, request: Request):
        resell_serializer = ResellSerializer(data=request.query_params)
        if resell_serializer.is_valid():
            try:
                reserve_id = resell_serializer.validated_data.get("reservation_id")
                new_price = resell_serializer.validated_data.get("new_price")
                response = self.resell_logic.make_reserve_resell(reserve_id, user=request.user, new_price=new_price)
                if isinstance(response, str):
                    return Response(data=response, status=status.HTTP_200_OK)
                else:
                    return Response(data=str(response), status=status.HTTP_503_SERVICE_UNAVAILABLE)

            except Exception as e:
                return Response(str(e), status=status.HTTP_400_BAD_REQUEST)