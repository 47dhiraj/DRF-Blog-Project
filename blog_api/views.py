from django.shortcuts import get_object_or_404
from rest_framework import generics
from blog.models import Post, Category

from .serializers import PostSerializer, CategorySerializer, CategoryPostSerializer
from users.serializers import CustomUserSerializer
from users.models import NewUser

from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, \
    IsAdminUser, DjangoModelPermissions, AllowAny

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters

from .mypagination import MyPageNumberPagination


from collections import namedtuple
CategoryPost = namedtuple('CategoryPost', ('posts', 'categories'))


class CategoryPostList(viewsets.ViewSet):
    def list(self, request):
        categorypost = CategoryPost(
            posts=Post.objects.all(),
            categories=Category.objects.all(),
        )

        serializer = CategoryPostSerializer(categorypost)
        return Response(serializer.data)



# ***** ----   PostUserWritePermission class chai auta custom permission class ho jun hamile create gareko ho  ----*****
class PostUserWritePermission(BasePermission):
    message = 'Editing & deleting of posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user  # yaha batw True return huncha


# ***** ---- Generics APIView class use garne ho vane chai yesari garna sakincha  ----*****

class CategoryList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer


class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]  
    serializer_class = PostSerializer
    pagination_class = MyPageNumberPagination

    # def get_queryset(self):
    #     return Post.objects.all()

    # Example 1 : Simple filter to filter the posts based on the loged in user
    #

    def get_queryset(self):
        user = self.request.user
        return Post.postobjects.all().order_by('-id').filter(
            author=user)  # particular user ko matra posts haru filter garera nikalne query lagako or filter user gareko vanam na


# For the Admin (Admin Part)

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Detail for the Post
class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def get_object(self, queryset=None, **kwargs): 
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, id=item)

    # def get_queryset(self):
    #     id = self.kwargs['pk']
    #     return Post.objects.filter(id=id)

    # def get_queryset(self):
    #     id = self.request.query_params.get('pk', None)      
    #     return Post.objects.filter(id=id)


# Editing the Post
class EditPost(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated, PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# Deleting the Post
class DeletePost(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# To get authenticated user
class GetUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        user = self.request.user
        return NewUser.objects.all().filter(user_name=user)


# To Search the PostList
class PostListDetailfilter(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title', '^category__name']  

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.

    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    # def get_queryset(self):
    #     return Post.objects.all()

