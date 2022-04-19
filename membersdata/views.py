# from django.http import HttpResponseRedirect
# from django.shortcuts import render
# from django.urls import reverse
from django.views import generic
from .models import Member

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'membersdata/index.html'
    context_object_name = 'member_objects'

    def get_queryset(self):
        return Member.objects.order_by('-id')