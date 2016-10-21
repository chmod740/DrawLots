"""DrawLots URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web.views import login, check_login, index, draw, get_my_draw, logout

urlpatterns = [
    url('^$', index),
    url(r'^admin/', admin.site.urls),
    url(r'^login.html', login),
    url(r'^check_login.html', check_login),
    url(r'^index.html', index),
    url(r'^draw.html', draw),
    url(r'^get_my_draw.html', get_my_draw),
    url(r'^logout.html', logout),
]
