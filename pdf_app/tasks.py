from celery import shared_task, states
import time
from PyPDF2 import PdfFileReader
from datetime import timedelta
from .models import Document
import base64, io

@shared_task
def celery_task(counter):
    email = "hassanzadeh.sd@gmail.com"
    time.sleep(30)
    return '{} Done!'.format(counter)

@shared_task
def extract_data_from_pdf(document_id,file):
    self = extract_data_from_pdf
    file = base64.b64decode(file)
    file = io.BytesIO(file)

    pdf = PdfFileReader(file)
    extracted_data = ''
    for page in pdf.pages:
        print(f'---------extracted data{dir(page)}', page.extractText())
        extracted_data += page.extractText()
    print('---------extracted data', extracted_data)
    document = Document.objects.get(id=document_id)
    document.data = extracted_data
    document.status = states.SUCCESS
    document.task_id = self.AsyncResult(self.request.id).task_id
    document.save()
    return '{} Done!'.format(document.name)
