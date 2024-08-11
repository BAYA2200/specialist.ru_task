from rest_framework import permissions, viewsets
from rest_framework.authentication import TokenAuthentication

from .models import BlogPost
from .permissions import PostBlogPermission
from .serializers import BlogPostSerializer



class BlogPostViewSet(viewsets.ModelViewSet):
    """
    Blog API endpoint to get list of blogs and create blogs and put blogs and delete blogs.
    """

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [PostBlogPermission, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
