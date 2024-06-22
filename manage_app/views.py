from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Manage

# 共通の親クラスを定義
class ManageBaseView(LoginRequiredMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['designer_choices'] = Manage.DESIGNER_CHOICES
        context['coder_choices'] = Manage.CODER_CHOICES
        #print(context)
        return context

class ManageList(ManageBaseView, ListView):
    model = Manage
    context_object_name = "topicks"

class ManageLoginView(LoginView):
    fields = "__all__"
    template_name = "manage_app/login.html"
    def get_success_url(self):
        return reverse_lazy("topicks")

class ManageCreate(ManageBaseView, CreateView):
    model = Manage
    fields = "__all__"
    success_url = reverse_lazy("topicks")

class ManageDetail(ManageBaseView, DetailView):
    model = Manage
    context_object_name = "topick"

class ManageUpdate(ManageBaseView, UpdateView):
    model = Manage
    fields = "__all__"
    success_url = reverse_lazy("topicks")

class ManageDelete(ManageBaseView, DeleteView):
    model = Manage
    fields = "__all__"
    success_url = reverse_lazy("topicks")
    context_object_name = "topick"

class PersonList(ManageBaseView, ListView):
    model = Manage
    template_name = "manage_app/person_list.html"
    context_object_name = "topicks"
    
    def get_queryset(self):
        person_type = self.kwargs['person_type']
        person_name = self.kwargs['person_name']
        if person_type == 'designer':
            return Manage.objects.filter(デザイナー名=person_name)
        elif person_type == 'coder':
            return Manage.objects.filter(コーダー名=person_name)
        else:
            return Manage.objects.none()
        
    def get_person_display_name(self, person_type, person_name):
        if person_type == 'designer':
            choices = dict(Manage.DESIGNER_CHOICES)
        elif person_type == 'coder':
            choices = dict(Manage.CODER_CHOICES)
        else:
            return person_name
        return choices.get(person_name, person_name)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        person_type = self.kwargs['person_type']
        person_name = self.kwargs['person_name']
        context['person_type'] = person_type
        context['person_name'] = person_name
        context['person_display_name'] = self.get_person_display_name(person_type, person_name)
        context['manage_list'] = self.get_queryset()
        return context
    
