"""theBlogOfTheUnThought URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from gestor_general import views
#Image upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.log_in),
    path("verificar_usuario/",views.verificar),
    path("foro/<str:sector>/",views.foro),
    path("Registrarse/",views.register),
    path("Registrarse/validar_registro/",views.validity_register),
    path("foro/add",views.new_post),
    path("foro/save",views.add_post),
    path("foro/personal/<str:user_name>",views.personal_post),
    path("post/read/<int:id>",views.read_post),
    path("add_ansewer/<int:id>",views.ansewer),
    path("render_ansewer/<int:id>",views.save_ansewer)
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
