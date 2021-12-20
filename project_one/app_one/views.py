from django import forms
import django
from django.http import request
from django.shortcuts import render, resolve_url
import app_one
from app_one.forms import formed
# from django.http import HttpResponse
from app_one.models import AccessRecord
# from . import forms

#code for forms.py file
def index(req):
    dic = {'n1':'hello world'}
    return render(req,'app_one/f_ind1.html',dic) 

def form_name_view(req):
    form =formed()


    if req.method == 'POST':
        form = formed(req.POST)

        if form.is_valid():
            form.save()
            
            return index(req)

        else:
            print("error")

    #         print("\nsucess..!")
    #         print("\nname:"+ form.cleaned_data['name'])
    #         print("\nemail:"+ form.cleaned_data['email'])
    #         print("\ntext:" + form.cleaned_data['comment'])
   
    return render(req, 'app_one/f_ind2.html', {'form':form})








# all code below is code before creating forms.py file

# when template is created
def info(args):
    web_list= AccessRecord.objects.order_by("date")
    dic ={'insert_me':web_list}
    return render(args, 'app_one/index.html', context=dic)
    # return HttpResponse("<em>HELLO YOU THERE<em>")
    
# def para(request):
#     return HttpResponse("this is a new project of web application using django!!!")