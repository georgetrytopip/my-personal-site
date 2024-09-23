from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import os


def my_info(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


def download_resume(request):

    filepath = settings.RESUME_PATH

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/pdf')
        response ['Content-Disposition'] = 'attachment; filename="resume.pdf"'
        return response

