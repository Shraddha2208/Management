from django.shortcuts import render,redirect
from .models import StudentModel
from .forms import StudentForm


# Create your views here.


def home(request):
    return render(request,"home.html")
def register(request):
    return render(request,"register.html")
def list(request):
    return render(request,"list.html")
def detail(request):
    return render(request,"detail.html")
def contact(request):
    return render(request,"contact.html")
def access(request):
    return render(request,'access.html')
    


def viewstudents(request):
    Student_list=StudentModel.objects.all()
    context={
        'Student_list':Student_list
        
    }
    return render(request,"display.html",context)

def CreateView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create')
    else:
        form =StudentForm()
        context = {
            'form':form
        }
        return render(request,'register.html',context)

def Retrieve_ListView(request):
    dataset = StudentModel.objects.all()
    return redirect('/data')
    return render(request,'list.html',{'dataset':dataset})
 
def Retrieve_DetailView(request,_id):
    try:
        data =StudentModel.objects.get(id =_id)

    except StudentModel.DoesNotExist:
        raise Http404('Data does not exist')
 
    return render(request,'detail.html',{'data':data})