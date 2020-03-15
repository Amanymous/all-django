
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from django.conf.urls import include #ye api url add kiya ha
# settings.py ma install_apps='rest_framework','api'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),#is ma api folder ka url diya ha ka url
    path('auth/', obtain_auth_token),
]
