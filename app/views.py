from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomUserCreationForm
from django.shortcuts import render,get_object_or_404,redirect
from app.models import Ert
from app.forms import ErtForm





def user_login(request):

    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/profile/')
         

        else:
            return HttpResponseRedirect('/login/')
            
    else:
        fm=AuthenticationForm()
        return render(request,'app/userlogin.html',{'form':fm})
                
  


  
                
def user_profile(request):

     return render(request,"app/profile.html",{'objectlist':Ert.objects.all()})

    
   
    
    
    
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
    
    
    
    
def user_register(request):
    form=CustomUserCreationForm
    if request.method=='POST':
        regForm=CustomUserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request,'User has been registered successfully.')
        else:
            messages.warning(request, 'User has Not registered successfully..')
    return render(request,'app/register.html',{'form':form})
    
    
    
    
def addErt(request):
    if(request.method=='POST'):
        ert_form=ErtForm(request.POST)
        if ert_form.is_valid():
            ert_form.save()
        return redirect('profile')
            
    else:
        ert_form=ErtForm()
    return render(request,"app/add_ert.html", {'form':ert_form })
    
  
  
def details(request,pk):
    context_object={'category' : get_object_or_404(Ert,pk=pk)}
    template_name="app/detail.html"
    return render(request, template_name,context_object)
 
 
 
def updateErt(request,pk):
    ert_object=get_object_or_404(Ert,pk=pk)
    ert_form=ErtForm(instance=ert_object)
    if(request.method=='POST'):
        ert_form=ErtForm(request.POST or None,instance=ert_object)
        if ert_form.is_valid():
            ert_form.save()
            return redirect('profile')
    return render(request, 'app/add_ert.html', {'form':ert_form })
    
    
    
def deleteErt(request, pk):
    delete_object=get_object_or_404(Ert,pk=pk)
    delete_object.delete()
    return redirect('profile')
    
    

