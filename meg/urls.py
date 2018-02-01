from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('sites/', include('sites.urls')),
    path('summary/', include('summary.urls')),
    path('summary-average/', include('summary.urls')),
    path('admin/', admin.site.urls),
]
