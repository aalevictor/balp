"""balp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from accounts.views import CheckLogin, VerifyUsers

urlpatterns = [
    path('', include('bal.urls')),
    path('admin/', admin.site.urls),
    path('bal/', include('bal.urls')),
    path('ocr/', include('ocr.urls')),
    path('user/', include('accounts.urls')),
    path('login', TokenObtainPairView.as_view()),
    path('check', CheckLogin.as_view()),
    path('verify', VerifyUsers.as_view()),
    path('refresh', TokenRefreshView.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
