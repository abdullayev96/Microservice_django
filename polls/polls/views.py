from rest_framework import generics
from .serializers import PollSerializer
from .models import Poll


class PollAPIView(generics.ListCreateAPIView):
	queryset = Poll.objects.all()
	serializer_class = PollSerializer