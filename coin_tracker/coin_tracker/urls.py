from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('portfolio.urls'), name='portfolio'),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
