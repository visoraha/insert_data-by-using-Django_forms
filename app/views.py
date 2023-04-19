from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def student_file(request):
    SFO=Student_form()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=Student_form(request.POST)
        if SFD.is_valid():
            sid=SFD.cleaned_data['sid']
            name=SFD.cleaned_data['name']
            mbno=SFD.cleaned_data['mbno']
            email=SFD.cleaned_data['email']
            SO=Student.objects.get_or_create(sid=sid,name=name,mbno=mbno,email=email)[0]
            SO.save()
            obs=Student.objects.all()
            d1={'obs':obs}
            return render(request,'display.html',d1)

    return render(request,'student_file.html',d)
