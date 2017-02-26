from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_view


urlpatterns = [

    url(r'^$', home_view, name='home'),

    url(r'^post/', include('post.urls')),

    url(r'^admin/', admin.site.urls),
]
