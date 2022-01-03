from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )
from rest_framework.schemas import get_schema_view  # hamro schema or endpoints haru dekhaucha
from rest_framework.documentation import include_docs_urls  # hamro endpoint dekhaune gui ho

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Simple JWT authentication url ho yo 
    # url for getting token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url for refreshing token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # URL for Django Provided Default Admin Panel
    path('admin/', admin.site.urls),

    # Using namespace in the include() allows you to include the same app more than once, with a different namespace. Here the blog app is included many times with different namespaces.
    path('', include('blog.urls')),

    # URL for Blog_API Application (api endpoints to entry point ho yo)
    path('api/', include('blog_api.urls')),

    # users app ko urls.py ma hit hanne url ho yo
    path('api/user/', include('users.urls')),

    # DRF le provide gareko login & logount garne authentication url ho
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url for schema generation
    path('schema/', get_schema_view(
        title="BlogAPI",
        description="API for the Blog Post",
        version="1.0.0"
    ), name='openapi-schema'),

    # url for gui document generation
    path('docs/', include_docs_urls(title='BlogAPI')),

    # Home Url
    path('', include('home.urls')),

    # login_signup urls
    path('', include('login_signup.urls')),

]

# yesari settings.py ma mention vako media directory chinauna ko lagi urlpattern lekhnu parcha
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
