from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Comment


# ======================================================================================================================
class CommentSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "product",
            "user",
            "parent",
            "body",
            "created_date",
            "detail_url",
            "list_url",
        ]
        read_only_fields = ["id", "user", "created_date"]

    def get_detail_url(self, obj):
        request = self.context.get("request")
        return reverse("comment-detail", kwargs={"pk": obj.pk}, request=request)

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("comment-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
