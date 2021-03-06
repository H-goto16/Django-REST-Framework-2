from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('API.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')), 
    path('account-confirm-email/', include('allauth.urls')), 
]
