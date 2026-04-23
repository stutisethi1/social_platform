from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def get_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)