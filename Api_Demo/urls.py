from django.contrib import admin
from django.urls import path,include
from api_app.views import showexp

from api_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_app.urls')),

]
