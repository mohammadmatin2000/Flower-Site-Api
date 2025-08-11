from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.password_validation import validate_password
from shop.models import PlantProduct
from order.models import OrderModels, CouponModels
from comments.models import Comment
from contact.models import ContactMessage, Newsletter
from accounts.models import Profile, User


# ======================================================================================================================
class AdminSecuritySerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(
        write_only=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "رمز عبور جدید با تاییدیه آن مطابقت ندارد."}
            )
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError("رمز عبور فعلی اشتباه است.")
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save()
        return user


# ======================================================================================================================
class AdminProfileSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["user", "first_name", "last_name", "image", "detail_url", "list_url"]

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-profile-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-profile-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class AdminUserSerializer(serializers.ModelSerializer):
    user_profile = AdminProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "type", "user_profile"]


# ======================================================================================================================
class AdminProductSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = PlantProduct
        fields = [
            "id",
            "name",
            "slug",
            "price",
            "status",
            "created_date",
            "updated_date",
            "detail_url",
            "list_url",
        ]

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-products-detail", kwargs={"slug": obj.slug})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-products-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class AdminOrderSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = OrderModels
        fields = "__all__"

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-orders-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-orders-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class AdminCouponSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = CouponModels
        fields = "__all__"

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-coupons-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-coupons-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class AdminCommentSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = "__all__"

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-comments-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-comments-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class AdminTicketSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = ContactMessage
        fields = "__all__"

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-tickets-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-tickets-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
class AdminNewsletterSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()
    list_url = serializers.SerializerMethodField()

    class Meta:
        model = Newsletter
        fields = "__all__"

    def get_detail_url(self, obj):
        request = self.context.get("request")
        url = reverse("admin-newsletters-detail", kwargs={"pk": obj.pk})
        return request.build_absolute_uri(url) if request else url

    def get_list_url(self, obj):
        request = self.context.get("request")
        return reverse("admin-newsletters-list", request=request)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context.get("view") and self.context["view"].action != "list":
            representation.pop("detail_url", None)
        else:
            representation.pop("list_url", None)
        return representation


# ======================================================================================================================
