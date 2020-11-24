from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import PostSerializer


# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Post.objects.filter(published=True)
    serializer_class = PostSerializer
