from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.decorators import login_required


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API documentation",
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    path(
        'swagger/',
        login_required(schema_view.with_ui('swagger', cache_timeout=0)),
        name='schema-swagger-ui'
    ),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout = 0)),
]
