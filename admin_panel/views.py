from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from accounts.models import User
from admin_panel.models import Client, Property, File, Agent
from django.views.generic import TemplateView, RedirectView
from django.contrib import messages

from admin_panel.forms import ClientForm, PropertyForm, FileForm, PaymentForm, AgentForm
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "admin/index.html")

@user_passes_test(lambda u: u.is_superuser)
def account(request: HttpRequest) -> HttpResponse:
    return render(request, "admin/account.html")

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class AgentView(LoginRequiredMixin, SuperuserRequiredMixin,TemplateView):
    template_name = "admin/agent.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['agent_data'] = Agent.objects.all()
        context['agent_form'] = AgentForm()
        return context
    
    def post(self, request):
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid() and not Agent.objects.filter(cnic=form.cleaned_data['cnic']).exists():
           form.save()
        else:
            messages.error(request, form.errors)
        return HttpResponseRedirect(self.request.path_info)

class AgentViewDelete(RedirectView):
    url = "/admin/agents"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        Agent.objects.get(cnic=kwargs['cnic']).delete()
        return super().get_redirect_url(*args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def updateAgent(request, cnic):
    agent = Agent.objects.get(cnic=cnic)
    form = AgentForm(instance=agent)
    context={'agent_form': form, 'agent_data':Agent.objects.all()}

    if request.method == 'POST':
        form = AgentForm(request.POST,request.FILES, instance=agent)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated Successfully')
            return redirect('/admin/agents')

    return render(request, 'admin/agent.html', context)


class UserView(TemplateView):
    template_name = "admin/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['data'] = User.objects.all()
        return context

class UserViewDelete(RedirectView):
    url = "/admin/users"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        instance = get_object_or_404(User, cnic=kwargs['cnic']) 
        instance.delete() 
        return super().get_redirect_url(*args, **kwargs)

class ClientView(LoginRequiredMixin, SuperuserRequiredMixin,TemplateView):
    template_name = "admin/client.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['client_data'] = Client.objects.all()
        context['client_form'] = ClientForm()
        return context
    
    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid() and not Client.objects.filter(cnic=form.cleaned_data['cnic']).exists():
            nm = form.cleaned_data['name']
            gu = form.cleaned_data['guardian']
            co = form.cleaned_data['contact']
            cn = form.cleaned_data['cnic']
            st = form.cleaned_data['status']
            client = Client(name=nm, guardian=gu, contact=co, cnic=cn, status = st)
            client.save()
        else:
            messages.error(request, 'This User already exists!')
        return HttpResponseRedirect(self.request.path_info)

class ClientViewDelete(RedirectView):
    url = "/admin/clients"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        Client.objects.get(cnic=kwargs['cnic']).delete()
        return super().get_redirect_url(*args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def updateClient(request, cnic):
    client = Client.objects.get(cnic=cnic)
    form = ClientForm(instance=client)
    context={'client_form': form, 'client_data':Client.objects.all()}

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated Successfully')
            return redirect('/admin/clients')

    return render(request, 'admin/client.html', context)


class PropertyView(LoginRequiredMixin, SuperuserRequiredMixin,TemplateView):
    template_name = "admin/property.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['property_data'] = Property.objects.all()
        context['property_form'] = PropertyForm()
        return context
    
    def post(self, request):
        form = PropertyForm(request.POST)
        if form.is_valid() and not Property.objects.filter(name=form.cleaned_data['name']).exists():
            form.save()
        else:
            messages.error(request, 'This Property already exists!')
        return HttpResponseRedirect(self.request.path_info)

class PropertyViewDelete(RedirectView):
    url = "/admin/property"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        Property.objects.get(plot=kwargs['plot']).delete()
        return super().get_redirect_url(*args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def updateProperty(request, plot):
    property = Property.objects.get(plot=plot)
    form = PropertyForm(instance=property)
    context={'property_form': form, 'property_data':Property.objects.all()}

    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated Successfully')
            return redirect('/admin/property')

    return render(request, 'admin/property.html', context)


class FileView(LoginRequiredMixin, SuperuserRequiredMixin,TemplateView):
    template_name = "admin/file.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['file_data'] = File.objects.all().order_by('file')
        context['file_form'] = FileForm()
        context['total'] = countTotal()
        return context
    
    def post(self, request):
        form = FileForm(request.POST)
        if form.is_valid() and not File.objects.filter(file=form.cleaned_data['file']).exists() and not File.objects.filter(property=form.cleaned_data['property']).exists():
            fi = form.cleaned_data['file']
            fi2 = form.cleaned_data['new_file']
            ag = form.cleaned_data['agent']
            cl = Client.objects.get(name=form.cleaned_data['client'].name, cnic = form.cleaned_data['client'].cnic)
            pr = Property.objects.get(plot=form.cleaned_data['property'].plot)
            st = form.cleaned_data['status']
            property = File(file=fi,new_file=fi2, agent=ag, client=cl, property=pr, status = st, payment = [])
            property.save()
        else:
            messages.error(request, 'ERROR in file creation!')
        return HttpResponseRedirect(self.request.path_info)
        
def countTotal():
    val = File.objects.all().order_by('file')
    re = []
    for va in val:
        sum=0
        for pa in va.payment:
            sum += int(pa[1])
        re.append([sum,int(va.property.amount)-int(sum)])
    print(re)
    return re

class FileViewDelete(RedirectView):
    url = "/admin/file"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        File.objects.get(file=kwargs['file']).delete()
        return super().get_redirect_url(*args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def updatePayment(request, file):
    property = File.objects.get(file=file)
    form = PaymentForm(instance=property)
    context={'file_form': form, 'file_data':File.objects.all()}

    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=property)
        if form.is_valid():
            property.payment.append([form.cleaned_data['payment_details'],form.cleaned_data['amount']]) 
            property.save()
            messages.info(request, 'Added Successfully')
            return redirect('/admin/file')

    return render(request, 'admin/file.html', context)

@user_passes_test(lambda u: u.is_superuser)
def updateFile(request, file):
    file_obj = File.objects.get(file=file)
    form = FileForm(instance=file_obj)
    context={'file_form': form, 'file_data':File.objects.all()}

    if request.method == 'POST':
        form = FileForm(request.POST, instance=file_obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'Updated Successfully')
            return redirect('/admin/file')
        else:
            print(form.errors.as_data())
        

    return render(request, 'admin/file.html', context)

