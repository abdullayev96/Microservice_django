from django.contrib import admin
from django.urls import path
from .views import VoteAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('vote/', VoteAPIView.as_view()),
]

