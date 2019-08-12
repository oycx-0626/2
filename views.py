from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import person_news
from .import models
# Create your views here.我本地上的mysql服务

def index(request):
    if request.method == 'GET':
        context = {}
        return render(request,'BIM计算器/index.html',context)
    if request.method == 'POST':
        # time = request.POST.get('time')
        height = str(request.POST.get('f_height'))
        weight = str(request.POST.get('f_weight'))
        bmi = float('%.2f'%(int(weight)/(int(height)/100)**2))
        models.person_news.objects.create(person_height=height,person_weight=weight,person_bmi=bmi)
        person_list = person_news.objects.filter(person_height=height)
        context = {
            'height': height,
            'weight': weight,
            'bmi': bmi,
            'person_list':person_list,
            # 'time':time
        }
        return render(request,'BIM计算器/index.html',context)

def delete(request):
    id = request.GET.get('id')
    models.person_news.objects.get(id=id).delete()
    return HttpResponseRedirect('/BIM计算器/index/')
