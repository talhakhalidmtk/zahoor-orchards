from django.http import  HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth import login,authenticate,logout
from .forms import UserCreationForm, UserLoginForm
from django.contrib import messages

class SignUpView(TemplateView):
    template_name = "customer/sign-up.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # first, call super get context data
        context['form'] = UserCreationForm()
        return context
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Registered Successfully. Please Sign In to continue.")
        else:
            messages.error(request, form.errors.as_text)
        return HttpResponseRedirect("/accounts/")


class SignInView(TemplateView):
    template_name = "customer/sign-in.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # first, call super get context data
        context['form'] = UserLoginForm()
        return context
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            password=request.POST["password"]
            cnic=request.POST["cnic"]
            user=authenticate(cnic=cnic,password=password)
            if user:
                login(request,user)
                messages.info(request,"Hello "+user.name)
                return HttpResponseRedirect("/")
            else:
                messages.error(request,"Invalid CNIC/Password")
                return HttpResponseRedirect("/accounts/")
                
        
