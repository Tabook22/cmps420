from django.urls import path
from .views import check_request

urlpatterns=[
    path('myrequest/',check_request),
    ]