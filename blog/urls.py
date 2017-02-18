from django.conf.urls import url
from django.contrib import admin
from post.views import home_view


urlpatterns = [
    
    url(r'^$', home_view),

    url(r'^admin/', admin.site.urls),
]
