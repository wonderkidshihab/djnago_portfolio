
from django.contrib import admin
from django.urls import path, include

from home import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include(urls)),
]
