from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from .dal import db
import os
import moz.settings as s
# Create your views here.

def upload_image(request):
    # need to get the image list
    if 'img_name' in request.session:
        files = request.session.get('img_name')
        seen = request.session.get('img_seen')
    else:
        # create the image list
        im = os.listdir(os.path.join(s.STATICFILES_DIRS[0], 'img'))
        request.session['img_name'] = im
    if request.method == 'GET':
        return render(request, 'upload_image.html', {})
    else:
        picture_of = request.POST['text_picture_of']
        has = request.POST['text_has']
        does = request.POST['text_does']
        db().PUT(isa=picture_of, has=has, does=does)
        return render(request, 'upload_image.html', {})
