from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reports.urls')),
    path('blog/', include('blog_accident.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

# ✅ Only add this in development (DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



# from django.contrib import admin
# from django.urls import path, include
# from django.conf.urls.i18n import i18n_patterns
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', include('reports.urls')),             # Main app
#     path('admin/', admin.site.urls),               # Admin panel
#     path('blog/', include('blog_accident.urls')),  # Blog app
#     path('i18n/', include('django.conf.urls.i18n'))  # Language switcher
# ]

# # Only add static files route when DEBUG = True
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
