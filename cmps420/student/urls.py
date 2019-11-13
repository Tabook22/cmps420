from django.urls import path
from .views import index, check_request, show_result
app_name = 'student'
urlpatterns = [
    path('index/', index, name='index'),
    path('showresult/', show_result),
    path('crq/', check_request)
]
