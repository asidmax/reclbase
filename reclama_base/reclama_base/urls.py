from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('reclbase.urls', namespace='')),
]

if settings.DEBUG:
    urlpatterns.append(path('statis/<path:path>', never_cache(serve)))