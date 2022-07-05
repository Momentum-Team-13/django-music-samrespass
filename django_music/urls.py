"""django_music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.urls import path, include
from djamming import views as site_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', site_page.front_page, name='front_page'),
    path('albums/<int:pk>', site_page.single_album, name='single_album'),
    path('albums/new', site_page.new_album, name='new_album'),
    path('albums/<int:pk>/delete', site_page.delete_album, name='delete_album'),
    path('albums/<int:pk>/edit/', site_page.edit_album, name='edit_album'),
    path('albums/new/track', site_page.new_track, name='new_track'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
