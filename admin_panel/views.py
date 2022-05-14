from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import View
from admin_panel.models import Client, Property, File
from django.views.generic import TemplateView, RedirectView
from django.contrib import messages

from admin_panel.forms import ClientForm, PropertyForm, FileForm

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "admin/index.html")

def account(request: HttpRequest) -> HttpResponse:
    return render(request, "admin/account.html")

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class ClientView(TemplateView):
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
            messages.info(request, 'This User already exists!')
        return HttpResponseRedirect(self.request.path_info)

class ClientViewDelete(RedirectView):
    url = "/admin/clients"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        Client.objects.get(cnic=kwargs['cnic']).delete()
        return super().get_redirect_url(*args, **kwargs)

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


class PropertyView(TemplateView):
    template_name = "admin/property.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['property_data'] = Property.objects.all()
        context['property_form'] = PropertyForm()
        return context
    
    def post(self, request):
        form = PropertyForm(request.POST)
        if form.is_valid() and not Property.objects.filter(plot=form.cleaned_data['plot']).exists():
            pl = form.cleaned_data['plot']
            si = form.cleaned_data['size']
            bl = form.cleaned_data['block']
            am = form.cleaned_data['amount']
            cat = form.cleaned_data['category']
            st = form.cleaned_data['status']
            property = Property(plot=pl, size=si, block=bl, amount=am, category = cat, status=st)
            property.save()
        else:
            messages.info(request, 'This Property already exists!')
        return HttpResponseRedirect(self.request.path_info)

class PropertyViewDelete(RedirectView):
    url = "/admin/property"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        Property.objects.get(plot=kwargs['plot']).delete()
        return super().get_redirect_url(*args, **kwargs)

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


class FileView(TemplateView):
    template_name = "admin/file.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['file_data'] = File.objects.all()
        context['file_form'] = FileForm()
        return context
    
    def post(self, request):
        form = FileForm(request.POST)
        if form.is_valid():
            # cl = form.cleaned_data['client']
            # messages.info(request, cl.cnic)
            fi = form.cleaned_data['file']
            ag = form.cleaned_data['agent']
            cl = Client.objects.get(name=form.cleaned_data['client'].name, cnic = form.cleaned_data['client'].cnic)
            pr = Property.objects.get(plot=form.cleaned_data['property'].plot)
            st = form.cleaned_data['status']
            property = File(file=fi, agent=ag, client=cl, property=pr, status = st)
            property.save()
            return HttpResponseRedirect(self.request.path_info)

class FileViewDelete(RedirectView):
    url = "/admin/file"
    def get_redirect_url(self, *args, **kwargs):
        url = self.request.path_info
        File.objects.get(file=kwargs['file']).delete()
        return super().get_redirect_url(*args, **kwargs)