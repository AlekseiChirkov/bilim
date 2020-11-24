from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import PostSerializer
# Create your views here.


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.filter(default=False)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)