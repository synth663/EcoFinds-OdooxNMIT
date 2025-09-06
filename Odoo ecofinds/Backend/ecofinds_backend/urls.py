from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line tells our project to look at the urls.py file inside our 'users' app
    # for any URL that starts with 'api/'.
    path('api/', include('users.urls')),
]
