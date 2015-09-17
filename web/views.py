from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from random import shuffle
from .dal import db
import os
import moz.settings as s
import pdb
# Create your views here.

def upload_image(request):
    # need to get the image list
    	
    if request.method == 'POST':
    
        image_name = request.POST['image_name']
        
        picture_of = request.POST['text_picture_of'].split(',')
        picture_of = [x.strip(' ') for x in picture_of]
        
        has = request.POST['text_has'].strip().split(',')
        has = [x.strip(' ') for x in has]
        
        does = request.POST['text_does'].split(',')
        does = [x.strip(' ') for x in does]
        
        db().PUT(image_name=image_name, isa=picture_of, has=has, does=does)
        
    if 'img_names' in request.session:
        print('name in session')
        if request.session['finished'] == True:
            return HttpResponse('FINISHED')
        files = request.session.get('img_names')
        seen = request.session.get('img_seens')
        # now work out which image to show
        
        print(seen)
        for k in range(0, len(seen)):
            print(k)
            if seen[k] == 0:
                seen[k] = 1
                request.session['img_seens'] = seen
                image_to_show = files[k]

                if k == len(seen)-1:
                    request.session['finished'] = True
                break
        # if we get here, we have finished iterating the images
        # return HttpResponse('finished')
    else:
        # create the image list
        print('arranging image list')
        im = os.listdir(os.path.join(s.STATICFILES_DIRS[0], 'img'))
        seen = [0] * len(im)
        print(im)
        print(seen)
        shuffle(im)
        request.session['img_names'] = im
        request.session['img_seens'] = seen
        request.session['finished'] = False
        seen[0] = 1
        image_to_show = im[0]
        
    
        
    return render(request, 'upload_image.html', {'image_to_show': image_to_show})
    
