from rest_framework import serializers
from ..models import Document

class PdfSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=127)
    file = serializers.FileField(required=True)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'status', 'created_at', 'updated_at')