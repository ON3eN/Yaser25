from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# عرض الصفحة الرئيسية من مجلد templates
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # الصفحة الرئيسية
    path('', include('store.urls')),
    path('order/', include('order.urls')),
    path('account/', include('account.urls')),
]

# دعم تحميل الصور عند تفعيل debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
