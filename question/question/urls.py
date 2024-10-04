from django.contrib import admin
from django.urls import path
from .views import QuestionAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('question/', QuestionAPIView.as_view()),
]
