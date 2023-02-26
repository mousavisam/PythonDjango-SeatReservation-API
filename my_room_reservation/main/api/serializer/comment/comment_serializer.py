from rest_framework import serializers

from ....model.comment_entity import Comment


class CommentSerializer(serializers.Serializer):
    receiver = serializers.CharField(max_length=100)
    message = serializers.CharField(max_length=500)
    parent = serializers.IntegerField(min_value=1, required=False)


class CommentResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'