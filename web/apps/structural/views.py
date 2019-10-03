from django.http import HttpResponse
from django.shortcuts import render
#from structuralanalysis.date.extraction import ExtractionDate
#from dataloader import DataLoader

app_name = 'structural'

def index(request):
    context = {
        "text": "DataLoader().getTextList().pop(0)",
        "json": ""
    }
    return render(request, app_name + '/templates/index.html', context)

def get(request):
    text = request.POST['text']
    context = {
        "text": text,
        "json": {
            "data": "ExtractionDate(text).getDate()"
        }
    }
    return render(request, app_name + '/templates/index.html', context)
