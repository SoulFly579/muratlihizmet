"""haber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.conf import settings
from django.urls import include,path
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('haber/<slug:slug>/<int:id>', views.haber, name='haber'),
    path('category/<slug:slug>/<int:id>', views.category_haber , name='category_haber'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('yazar/', views.yazar, name='yazar'),
    path('kunye/', views.kunye, name='kunye')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)