from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from mainapp.models import PostNews, UK


class IndexList(LoginRequiredMixin, ListView):
    model = PostNews
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная | ООО Новый город"
        context["news"] = PostNews.get_items()[:4]
        return context


class ContactList(LoginRequiredMixin, ListView):
    model = UK
    template_name = "mainapp/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты | ООО Новый город"
        context["contact"] = UK.get_item(1)
        return context


def main(request):
    return render(request, "mainapp/index.html")


def products(request):
    return render(request, "mainapp/products.html")


def contact(request):
    return render(request, "mainapp/contact.html")
