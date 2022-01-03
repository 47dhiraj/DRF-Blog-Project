from django.urls import path

from . import views

urlpatterns = [

    path('blog/', views.BlogTemplateView.as_view(), name='blog'),

    path('add_blog/', views.BlogAddTemplateView.as_view(), name='add_blog'),

    path('edit_blog/<int:pk>/', views.BlogEditTemplateView.as_view(), name='edit_blog'),

    path('blog_detail/<int:pk>/', views.BlogDetailTemplateView.as_view(), name='blog_detail')

]
