from django.shortcuts import HttpResponse,render,redirect
from messageapp.models import Msg
from django.shortcuts import get_object_or_404

# Create your views here.

def testing(request):
    return HttpResponse("hello linked succesufully")


def create(request):
    if request.method=='GET':
     return render(request,'create.html')
    else:
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        # return HttpResponse("data inserted successfully")
        return redirect('/dashboard')
    
def dashboard(request):
    m=Msg.objects.all()
    # print(m)
    
    # return HttpResponse("data fetched from database")
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    # print("id to be deleted")
    # return HttpResponse('id to be deleted'+rid)
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    # print("id to be edited :", rid)
    # return HttpResponse("id to be edited" +rid)
    if request.method=='GET':
        m = get_object_or_404(Msg, id=rid)
        # context={}
        # context['data']=m
        return render(request,'edit.html',{'data':m})
    else:
         n=request.POST['uname']
         mail=request.POST['uemail']
         mob=request.POST['mobile']
         msg=request.POST['msg']
         k= Msg.objects.filter(id=rid).update(name=n,email=mail,mobile=mob,msg=msg)
        #  k.save()
         return redirect('/dashboard')
     
# def updatedata(request,rid):
#     d.Msg     