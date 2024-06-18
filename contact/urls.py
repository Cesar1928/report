from django.urls import path
from .views import Contact, generar_reporte_productos, ReportePersonalizadoExcel
from contact import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('reporte', views.generar_reporte_productos, name='reporte'),
    path('reporteexcel/',ReportePersonalizadoExcel.as_view(), name = 'reporteexcel'),
    #path('enviarcorreo/',views.enviarcorreo, name = 'enviarcorreo'),
    path("contact", views.Contact, name ="contact" ),
    path('admin/', admin.site.urls),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
