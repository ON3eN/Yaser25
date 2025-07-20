from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),       # الصفحة الرئيسية عبر store/views.py
    path('order/', include('order.urls')),
    path('account/', include('account.urls')),
]

# دعم تحميل الصور أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
