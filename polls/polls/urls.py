from django.contrib import admin
from django.urls import path
from .views import PollAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('poll/', PollAPIView.as_view()),
]
