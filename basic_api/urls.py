#basic_api/urls.py
from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from basic_api import views
urlpatterns = [
    path('', views.API_objects.as_view()),
    path('<int:pk>/', views.API_objects_details.as_view()),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
