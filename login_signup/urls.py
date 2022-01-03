from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginTemplateView.as_view(), name='login'),
    path('signup/', views.SingnupTemplateView.as_view(), name='signup'),

]
