from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='home'), name='root_redirect'),
    path('mealbook/', include('mealapp.urls')),
    path('admin/', admin.site.urls),
]
