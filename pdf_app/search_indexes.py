from haystack import indexes
from .models import Document
from django.utils import timezone


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
   text = indexes.CharField(
      document=True, use_template=True,
      template_name="search/indexes/pdf_app/pdf_app_text.txt"
   )
   id = indexes.IntegerField(model_attr="id")
   name = indexes.CharField(model_attr="name")
   status = indexes.CharField(model_attr="status")
   data = indexes.CharField(model_attr="data")

   created_at = indexes.DateTimeField(model_attr='created_at')
   updated_at = indexes.DateTimeField(model_attr='updated_at')
   
   def get_model(self):
      return Document

   def index_queryset(self, using=None):
      return self.get_model().objects.all()