from django.http import HttpResponse
from django.shortcuts import render
from .models import Member

# Create your views here.
def index(request):
    first_two_members = Member.objects.order_by('-id')[:5]
    context = {'first_two_members': first_two_members}
    return render(request, 'membersdata/index.html', context)