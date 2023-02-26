from django.urls import path

from ...controller.comment.comment_controller import CommentController

urlpatterns = [
    path('create/', CommentController.as_view({'post': 'post'}), name='create_comment'),
    path('list/', CommentController.as_view({'get': 'get'}), name='comment_list'),
]