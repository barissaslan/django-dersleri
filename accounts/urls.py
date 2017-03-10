from django.conf.urls import url
from .views import *

app_name = "accounts"

urlpatterns = [

    url(r'^login/$', login_view, name="login"),

]
