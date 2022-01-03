from django.urls import path
from .views import PostList, PostListDetailfilter, CreatePost, EditPost, AdminPostDetail, DeletePost, CategoryList, \
    GetUser, CategoryPostList
from . import views
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()                                    # Creating router object
# router.register('', PostList, basename='post')              # router handling all the route or url path automatically for all the action handler used in PostList ViewSet  # hamile yaha single url route dekhya chau but it actually contain multiple route or url path
# urlpatterns = router.urls

urlpatterns = [

    # Url for listing posts
    path('', PostList.as_view(), name='list_post'),

    path('categorylist/', CategoryList.as_view(), name='category_list'),

    path('categorypostlist/', CategoryPostList.as_view({'get': 'list'}), name='category_post_list'),
    
    # URL For Admin (Authenticated User)
    path('admin/create/', CreatePost.as_view(), name='create_post'),
    path('admin/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='post_detail'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),



    path('getuser/', GetUser.as_view(), name='get_user'),

    # url for search filter facility
    path('search/', PostListDetailfilter.as_view(), name='search_post'),


]
