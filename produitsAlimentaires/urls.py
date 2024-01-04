"""
URL configuration for produitsAlimentaires project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from my_blog.views import home,detail,search,contact,Apropos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"), #root for http://127.0.0.1:8000/
    path('contact/', contact, name="contact"),
    path('Apropos/', Apropos, name="Apropos"),
    path("produit/<int:id_produit>", detail, name="detail"),
    path("produit/recherche", search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
