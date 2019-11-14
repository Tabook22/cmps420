from django.urls import path
from .views import index, check_request, show_result, show_wind
app_name = 'student'
urlpatterns = [
    path('index/', index, name='index'),
    path('showwind/', show_wind),
    path('showresult/', show_result),
    path('crq/', check_request)
]
