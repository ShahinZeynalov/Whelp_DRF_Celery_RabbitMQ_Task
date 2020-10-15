from ..serializers.haystack_serializers import DocumentHaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from ..models import Document
from ..search_indexes import DocumentIndex
from rest_framework.permissions import AllowAny, IsAuthenticated

class DocumentSearchView(HaystackViewSet):
    index_models = [Document]
    serializer_class = DocumentHaystackSerializer
    permission_classes = [IsAuthenticated]