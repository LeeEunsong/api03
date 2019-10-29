from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

'''
# ReadOnlyModelViewSet은 말 그대로 ListView, DetailView의 조회만 가능

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


'''

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        return HttpResponse("얍")
