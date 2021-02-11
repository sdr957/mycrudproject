from django.shortcuts import render,HttpResponseRedirect
from .forms import Userform
from .models import User

def add_show(request):
    if request.method=='POST':
        fm=Userform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            show=User(name=nm,email=em,password=pw)
            print(fm.cleaned_data['name'])
            show.save()
    else:
        fm=Userform()
    stud=User.objects.all()
    return render(request,'enroll/home.html',{'form':fm,'stu':stud})

    # this function will delete
def delete_data(request, id):

    if request.method=='POST':
            pi=User.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=Userform(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
            pi=User.objects.get(pk=id)
            fm=Userform(instance=pi)

    return render(request,'enroll/update.html',{'form':fm})
    # return render(request,'enroll/update.html', context=form)