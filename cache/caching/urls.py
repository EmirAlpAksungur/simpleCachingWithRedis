from django.urls import path
from caching.views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='test-url'),
]