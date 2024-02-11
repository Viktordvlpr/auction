from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from docutils.nodes import document
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
      path('', RedirectView.as_view(url='/website/', permanent=True)),
      path('admin/', admin.site.urls),
      path('website/', include('website.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
