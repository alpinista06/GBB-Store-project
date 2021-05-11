"""marioshop URL Configuration

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
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView

from .views import AccountBalanceView, GetImportUsers

admin.autodiscover()

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    path("admin/", admin.site.urls),
    path("account-balance/", AccountBalanceView.as_view(), name="account-balance"),
    path("dashboard/accounts/", apps.get_app_config("accounts_dashboard").urls),
    path("", include("tools.urls")),
    path("", include(apps.get_app_config("oscar").urls[0])),
    #path("import-new-users/", ImportTestView.as_view(), name="import-new-users-view"),
    path("import-new-users/", GetImportUsers, name="import-new-users-view"),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path("404", TemplateView.as_view(template_name="404.html")),
        path("500", TemplateView.as_view(template_name="500.html")),
    ]
