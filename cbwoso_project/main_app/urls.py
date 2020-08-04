
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employerList, name="employerlist" ),
    path('employerform/', views.employerForm, name="employerform" ),
    path('<int:id>/', views.employerForm, name="employeredit" ),
    path('delete/<int:id>/', views.employerDelete, name="employerdelete" ),
]