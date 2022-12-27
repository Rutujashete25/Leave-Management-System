from django.shortcuts import render
from .models import CustomUser,Role,Leaves
from .forms import RegistrationForm
from django.views import View
from django.urls import reverse_lazy,reverse
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.db.models import Q



class RegistrationView(CreateView):
    model = CustomUser
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'

    def form_valid(self,form,*args,**kwargs):
        user = form.save(commit=False)
        role = Role.objects.get(pk=self.kwargs['pk']) # this will assign instance of Role that means instance of staff or hod
        user.role_id = role # here we are assigning that unstance to the users role id
        user.set_password(form.cleaned_data['password']) #to format data into particular form i.e. hashable
        user = form.save()
        return redirect('login')


class customlogin(View):
    def get(self,*args,**kwargs):
        form = AuthenticationForm()
        return render(self.request, 'accounts/login.html',{'form':form})

    def post(self,request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            umail = form.cleaned_data.get('username')
            upass = form.cleaned_data.get('password')
            user = authenticate(username=umail,password=upass)
            if user  is not None :
                login(self.request, user) 
                if user.role_id.role_name == "HOD":
                    return redirect('hod-dashboard')
                return redirect('staff-dashboard') 
        return redirect('login')     
            
def home(request):
    role=Role.objects.all()
    return  render(request, 'accounts/home.html',{'roles':role})


