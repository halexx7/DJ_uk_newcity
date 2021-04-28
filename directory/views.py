from mainapp.models import Appartament, City, House, Street, UserProfile, Services, ServicesCategory

from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db import transaction

from directory.forms import ServicesCategoryEditForm, ServicesEditForm, CityEditForm, StreetEditForm
from directory.forms import HouseEditForm, AppartamentsEditForm, AppartamentFormset

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
    success_url = reverse_lazy("directory:services_update")
    form_class = ServicesEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Тариф/редактирование"
        return context


class ServicesDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    template_name = "directory/services_delete.html"
    success_url = reverse_lazy("directory:list")

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
    success_url = reverse_lazy("directory:list")
    form_class = StreetEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["city"] = self.kwargs["pk"]
        context["title"] = "Улица/создание"
        return context


class StreetUpdateView(LoginRequiredMixin, UpdateView):
    model = Street
    template_name = "directory/street_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = StreetEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["city"] = self.kwargs["pk"]
        context["title"] = "Улица/редактирование"
        return context


class StreetDeleteView(LoginRequiredMixin, DeleteView):
    model = Street
    template_name = "directory/street_delete.html"
    success_url = reverse_lazy("directory:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Улица/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


'''
=========
  HOUSE
=========
'''
class HouseListView(LoginRequiredMixin, ListView):
    model = House
    template_name = "directory/house.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        context['street'] = get_object_or_404(Street, pk=self.kwargs['pk'])
        context['house'] = House.objects.filter(street__pk=self.kwargs['pk']).order_by('street')
        return context


class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    template_name = "directory/house_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = HouseEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Дом/создание"
        return context


class HouseUpdateView(LoginRequiredMixin, UpdateView):
    model = House
    template_name = "directory/house_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = HouseEditForm

    def get_queryset(self):
        return House.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Дом/редактирование"

        if self.request.POST:
            context['appartament_form'] = AppartamentFormset(self.request.POST, instance=self.object)
        else:
            context['appartament_form'] = AppartamentFormset(instance=self.object)

        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = AppartamentFormset(self.request.POST)

        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        
        return self.form_invalid(form, formset)


    def form_valid(self, form, appartament_form):
        """
        Called if all forms are valid. Creates a Author instance along
        with associated books and then redirects to a success page.
        """
        with transaction.atomic():
            self.object = form.save()
            appartament_form.instance = self.object
            appartament_form.save()

        return HttpResponseRedirect(self.get_success_url())
    


class HouseDeleteView(LoginRequiredMixin, DeleteView):
    model = House
    template_name = "directory/house_delete.html"
    success_url = reverse_lazy("directory:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Дом/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



'''
================
  APPARTAMENTS
================
'''
class AppartamentsListView(LoginRequiredMixin, ListView):
    model = Appartament
    template_name = "directory/appartaments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['house'] = get_object_or_404(House, pk=self.kwargs['pk'])
        context['appartaments'] = Appartament.objects.filter(house__pk=self.kwargs['pk']).order_by('house')
        return context


class AppartamentsCreateView(LoginRequiredMixin, CreateView):
    model = Appartament
    template_name = "directory/appartaments_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = AppartamentsEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Квартира/создание"
        return context


class AppartamentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Appartament
    template_name = "directory/appartaments_update.html"
    success_url = reverse_lazy("directory:list")
    form_class = AppartamentsEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Квартира/редактирование"
        return context
    


class AppartamentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Appartament
    template_name = "directory/appartaments_delete.html"
    success_url = reverse_lazy("directory:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Квартира/удаление"
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())