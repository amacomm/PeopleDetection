from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import base64
from django.views.decorators.csrf import csrf_exempt
from . import found

def index(request):
    return HttpResponse("Сервис отмечающий области вокруг людей на изображеинии, для работы воспользуйтесть /recognize")

@csrf_exempt
def recognize(request):
    if request.method == 'POST':
        image=base64.b64decode(request.POST["image"])
        filename = request.POST["name"]
        with open("./in/"+filename, 'wb') as f:
            f.write(image)
        output, count = found.Find(filename)
        res={}
        with open(output, "rb") as image_file:
            res = {
                "image": base64.b64encode(image_file.read()).decode('ascii'),
                "count": count
                }
        return JsonResponse(res)
    else:
        return HttpResponse("Отправьте изображеие и название файла POST запросом в виде словаря: {'image': *base64_format_image*, 'name': *image_name_with_expansion* }, результат прийдёт в виде json: {'image': *base64_format_image*, 'count': *count_of_people* }")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('recognize', recognize, name='recognize'),
]
