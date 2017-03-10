from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^$', home_view, name='home'),

    url(r'^post/', include('post.urls')),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)