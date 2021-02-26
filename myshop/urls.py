# from django.conf.urls import  url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
# from django.conf.urls import include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('account/', include('account.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
