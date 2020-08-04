from django.urls import path, include
from . import views
from rest_framework import routers
import sys

router = routers.DefaultRouter()
router.register('employer', views.EmployerView)
router.register('contacts', views.ContactsView)

urlpatterns = [
    path('', include(router.urls)),
    path(r'xls/', views.export_xls, name='export_xls'),

]
