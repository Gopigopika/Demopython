from django.shortcuts import render
from .models import place,btable


# Create your views here.
def index(request):
    obj=place.objects.all()
    sub=btable.objects.all()
    context={
        'results':obj,
        'blogs':sub,
    }


    return render(request,'index.html',context)

#def blog(request):
 #   ob=blogt.objects.all()
  #  return render(request,'index.html',{'blogs':ob})