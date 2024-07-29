from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('banks/', include('banks.urls')),
    path('', RedirectView.as_view(pattern_name='list_banks', permanent=False), name='root_redirect'),
]
