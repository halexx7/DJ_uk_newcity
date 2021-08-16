from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from mainapp.models import UK, PostNews


class IndexList(ListView):
    model = PostNews
    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная | ООО Новый город"
        context["news"] = PostNews.get_items()[:4]
        return context


class ContactList(ListView):
    model = UK
    template_name = "mainapp/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты | ООО Новый город"
        context["contact"] = UK.get_item(1)
        return context


class NewstList(ListView):
    model = PostNews
    paginate_by = 10
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Новости | ООО Новый город"
        context["news"] = PostNews.get_items()
        return context
