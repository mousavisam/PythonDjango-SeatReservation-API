from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from ....logic.comment.comment_logic import CommentLogic
from ....api.serializer.comment.comment_serializer import CommentSerializer, CommentResponseSerializer


class CommentController(ViewSet):

    def __init__(self):
        super().__init__()
        self.comment_logic = CommentLogic()

    @extend_schema(
        request=CommentSerializer,
        tags=["Comment"],
        responses={200: str},
    )
    def post(self, request: Request):
        comment_serializer = CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            try:
                receiver = comment_serializer.validated_data.get("receiver")
                sender = request.user
                message = comment_serializer.validated_data.get("message")
                parent = comment_serializer.validated_data.get("parent", None)
                self.comment_logic.save_comments(receiver, sender, message, parent)

                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        tags=["Comment"],
        responses={200: CommentResponseSerializer},
    )
    def get(self, request: Request):
        try:
            sender_comments = self.comment_logic.get_comments_by_sender(sender=request.user)
            serialized_data = CommentResponseSerializer(sender_comments, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)