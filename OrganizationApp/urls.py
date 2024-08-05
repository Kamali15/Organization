from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orglist',OrganizationList.as_view(),name="org-list"),
    path('orgdetail/<int:pk>',OrganizationDetail.as_view(),name="org-detail"),

    path('suborglist',SubOrganizationList.as_view(),name="suborg-list"),
    path('suborgdetail/<str:pk>',SubOrganizationDetail.as_view(),name="suborg-detail"),

    path('divlist',DivList.as_view(),name="div-list"),
    path('divdetail/<str:pk>',DivDetail.as_view(),name="div-detail"),
    
    path('subdivlist',SubdivList.as_view(),name="subdiv-list"),
    path('subdivdetail/<str:pk>',SubdivDetail.as_view(),name="subdiv-detail"),

    path('emplist',EmpList.as_view(),name="emp-list"),
    path('empdetail/<str:pk>',EmpDetail.as_view(),name="emp-detail"),
]
