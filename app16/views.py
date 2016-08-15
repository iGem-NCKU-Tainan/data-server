from django.http import HttpResponse, HttpResponseForbidden
from django.utils import timezone
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.core import serializers

import requests
import datetime
import json
import uuid
import requests
import mimetypes
from app16.models import Data

@csrf_exempt
def index(request):
    if request.method == 'POST':
        req = request.POST
        data = Data(
            serialnum=req.get('Serialnum'),
            time=req.get('Time'),
            result=req.get('Result')
        )

        data.save()
        return HttpResponse(status=200)

    elif request.method == 'GET':
        response_data = []
        for d in Data.objects.all():
            response_data.append(model_to_dict(d))

        return HttpResponse(json.dumps(response_data), content_type="application/json")

    else:
        return HttpResponse(status=400)

