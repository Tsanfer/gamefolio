"""gamefolio URL Configuration

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
# from django.urls import include, path, reverse
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
# from registration.backends.simple.views import RegistrationView

from gamefolio_app import views

handler404 = 'gamefolio_app.views.handler404'
urlpatterns = [
    path('', views.IndexView.as_view(), name ="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('gamefolio/', include('gamefolio_app.urls', namespace='gamefolio')),
]+ static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
