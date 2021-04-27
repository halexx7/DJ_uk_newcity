from django import forms
from django.forms.formsets import formset_factory
from mainapp.models import Appartament, City, Street, UserProfile, Services, ServicesCategory
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from directory.forms import ServicesCategoryEditForm, ServicesEditForm, CityEditForm, StreetEditForm

class DirectoryList(LoginRequiredMixin, ListView):
    model = UserProfile
    template_name = "directory/directory_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = ServicesCategory.objects.all()
        data['city'] = City.objects.all()
        return data


'''
================
PRODUCT CATEGOTY
================
'''
class ServicesCategoryCreateView(LoginRequiredMixin, CreateView):
    model = ServicesCategory
    template_name = "directory/category_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = ServicesCategoryEditForm


class ServicesCategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = ServicesCategory
    template_name = "directory/category_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = ServicesCategoryEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Категории/редактирование"
        return context


class ServicesCategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = ServicesCategory
    template_name = "directory/category_delete.html"
    success_url = reverse_lazy("directory:list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



'''
=========
SERVICES
=========
'''
class ServicesListView(LoginRequiredMixin, ListView):
    model = Services
    template_name = "directory/services.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(ServicesCategory, pk=self.kwargs['pk'])
        context['services'] = Services.objects.filter(category__pk=self.kwargs['pk']).order_by('name')
        return context


class ServicesCreateView(LoginRequiredMixin, CreateView):
    model = Services
    template_name = "directory/services_update.html"
    success_url = reverse_lazy("directory:services")
    form_class = ServicesEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Тариф/создание"
        return context


class ServicesUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    template_name = "directory/services_update.html"
    success_url = reverse_lazy("directory:services")
    form_class = ServicesEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Тариф/редактирование"
        return context


class ServicesDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = "directory/services_delete.html"
    success_url = reverse_lazy("directory:services")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Тариф/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



'''
==========
   CITY
==========
'''
class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    template_name = "directory/city_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = CityEditForm


class CityUpdateView(LoginRequiredMixin, UpdateView):
    model = City
    template_name = "directory/city_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = CityEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Города/редактирование"
        return context

class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = "directory/city_delete.html"
    success_url = reverse_lazy("directory:list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


'''
==========
  STREET
==========
'''
class StreetListView(LoginRequiredMixin, ListView):
    model = Street
    template_name = "directory/streets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['city'] = get_object_or_404(City, pk=self.kwargs['pk'])
        context['streets'] = Street.objects.filter(city__pk=self.kwargs['pk']).order_by('street')
        return context


class StreetCreateView(LoginRequiredMixin, CreateView):
    model = Street
    template_name = "directory/street_update.html"
    success_url = reverse_lazy("directory:streets")
    form_class = StreetEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Улица/создание"
        return context


class StreetUpdateView(LoginRequiredMixin, UpdateView):
    model = Street
    template_name = "directory/street_update.html"
    success_url = reverse_lazy("directory:streets")
    form_class = StreetEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Улица/редактирование"
        return context


class StreetDeleteView(LoginRequiredMixin, DeleteView):
    model = Street
    template_name = "directory/street_delete.html"
    success_url = reverse_lazy("directory:streets")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Улица/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())