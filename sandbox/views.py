from django.shortcuts import render
from django.views.generic.base import TemplateView
from sandbox.models import Person, Group, Membership

class SandboxView(TemplateView):
    template_name = "sandbox.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['persons'] = Person.objects.all().prefetch_related('group_set')
        context['persons'] = Person.objects.all()
        context['groups'] = Group.objects.all().prefetch_related('members')
        return context
