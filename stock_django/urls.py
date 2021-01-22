from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', include('stock_app.urls'))
]

# url mapping for static objects
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
