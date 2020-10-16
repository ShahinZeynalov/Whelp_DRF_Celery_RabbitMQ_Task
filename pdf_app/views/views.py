from ..serializers.serializers import (
    PdfSerializer, DocumentSerializer
)
from django.shortcuts import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import get_user_model
from ..tasks import extract_data_from_pdf
import re
import base64
from ..models import Document
from drf_yasg2.utils import no_body, swagger_auto_schema


class CreateDocumentAPIView(APIView):
    serializer_class = PdfSerializer
    permission_classes = (IsAuthenticated, )

    @swagger_auto_schema(request_body=PdfSerializer)
    def post(self, request):
        pdf_file_pattern = re.compile(r'.*\.pdf')
        if pdf_file_pattern.match(request.data.get('file').name):
            document = Document()
            document.user = request.user
            document.name = request.data.get('file').name
            document.save()
            file = base64.b64encode(request.FILES.get('file').read())
            data = extract_data_from_pdf.delay(document.id, file)
            document.status = data.status
            document.save()
            return Response({
                'message': 'pdf file processing...',
                'status': '201',
                'data': {
                    'document_id': document.id,
                }
            })
        return Response({
            'message': 'Please select a pdf file',
            'status': '422'
        })

class RetrieveDocumentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = (IsAuthenticated, )
