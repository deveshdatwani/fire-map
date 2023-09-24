from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import io

# Create your views here.

def index(request):
    return render(request, "map.html")

@csrf_exempt 
def video(request):
    files = request.FILES
    img = files['media'].file
    # dataBytesIO = io.BytesIO(img)
    img_opened = Image.open(img)
    img_opened.show()
    # print(type(vid['media']))
    return HttpResponse("request received")
