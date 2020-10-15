from drf_haystack.serializers import HaystackSerializer
from ..models import Document
from ..search_indexes import DocumentIndex

class DocumentHaystackSerializer(HaystackSerializer):
    
    class Meta:
      index_classes = [DocumentIndex]
      fields = [
         'id', 'name', 'data'
      ]
