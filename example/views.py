from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Index(request):
    template = loader.get_template('index.html')
    context = {
        'title' : 'Belajar Django',
        'content_body' : 'Belajar',
    }

    return HttpResponse(template.render(context, request))