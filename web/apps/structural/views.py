from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from extractionfacts import ExtractionOffer
from jsonencoder import JsonEncoder

app_name = 'structural'

def index(request):
    context = {
        "text": "",
        "json": ""
    }
    return render(request, app_name + '/templates/index.html', context)

def get(request):
    text = request.POST['text']
    extractionOffer = ExtractionOffer(text)
    facts = extractionOffer.getFacts()
    context = {
        "text": text,
        "json": {
            "country": facts.Country,
            "city": facts.City,
            "StartDate": facts.StartDate,
            "EndDate": facts.EndDate,
        }
    }
    return render(request, app_name + '/templates/index.html', context)


@csrf_exempt
def apioffer(request):
    data = JsonEncoder().convert_to_object(request.body.decode('utf-8'))
    text = data['text']
    extractionOffer = ExtractionOffer(text)
    json = extractionOffer.getJson()
    return HttpResponse(json)