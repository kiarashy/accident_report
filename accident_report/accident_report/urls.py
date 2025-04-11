from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

# urlpatterns = [
#     path('i18n/', include('django.conf.urls.i18n')),  # Keeps language switch working
# ]

urlpatterns = [
    path('', include('reports.urls')),  # Home is in reports app
    path('admin/', admin.site.urls),
    path('blog/', include('blog_accident.urls')),  # Blog routing
    path('i18n/', include('django.conf.urls.i18n')),
]