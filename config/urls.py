from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import render
from django.conf.urls.static import static


from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail import urls as wagtail_urls

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('social/', include('social_django.urls', namespace="social")),
    path('users/', include('users.urls')),
    path('django-admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('', include(wagtail_urls)),  # Wagtail handles all root and subpages
] 

if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
