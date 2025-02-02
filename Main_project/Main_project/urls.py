"""
URL configuration for Main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('admin-dashboard/', include('adminDashboard.urls')),
    path('advance-payment-form/', include('advancePF.urls')),
    path('', include('homepage.urls')),
    path('budget-forms/', include('LowHighBudget.urls')),
    path('purchase-order-form/', include('purchase_order.urls')),
    path('vicechancellor-dashboard/', include('viceChancellor.urls')),
    path('vendor-management-dashboard/', include('vmdashboard.urls')),
    path('about/', include('cseDept.urls')),
    path('login/', include('login.urls')),
    path('registrar-dashboard/', include('registrar.urls')),
    path('hod-dashboard/', include('hodDashboard.urls')),
    path('finance-dashboard/', include('financeManagement.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
