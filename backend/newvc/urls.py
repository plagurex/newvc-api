"""
URL configuration for newvc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path('admin', admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar
    # Добавить к списку urlpatterns список адресов из приложения debug_toolbar:
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),) 
    # 3. Статика Django
    urlpatterns += static(
        settings.STATIC_URL, 
        document_root=settings.STATIC_ROOT
    )
    
    # 4. КОРЕНЬ (/) → index.html
    urlpatterns += [
        path('', serve, {
            'document_root': settings.BASE_DIR / 'site',
            'path': 'index.html'
        }),
    ]
    
    # 5. Остальные файлы из site/
    urlpatterns += [
        re_path(r'^(?P<path>.+)$', serve, {
            'document_root': settings.BASE_DIR / 'site',
        }),
    ]