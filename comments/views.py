from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# extending the ListAPIView means we won't have to write the get method
# and the CreateAPIView takes care of the post method
class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in
    """
    serializer_class = CommentSerializer
    # we don't want anonymous users to comment
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):  # make comments associated with a user upon creation
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
