from django.urls import path

from . import views

app_name = 'spotreserve'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:spot_identification>/spotdetail/', views.spotdetail, name='spotdetailurl'),
]