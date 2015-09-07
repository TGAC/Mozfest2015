from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .dal import db
# Create your views here.

def upload_image(request):
    if request.method == 'GET':
        return render(request, 'upload_image.html', {})
    else:
        picture_of = request.POST['text_picture_of']
        has = request.POST['text_has']
        does = request.POST['text_does']
        db().PUT(isa=isa, has=has, does=does)
        return render(request, 'upload_image.html', {})
