from rest_framework import serializers
from .models import ContactMessage
# ======================================================================================================================
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'subject', 'message', 'created_date', 'updated_date']
        read_only_fields = ['created_date', 'updated_date']
# ======================================================================================================================