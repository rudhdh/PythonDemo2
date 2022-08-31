from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from travelapp import views
from travelproject1 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travelapp.urls')),
    path('credentials/', include('credentials.urls')),
    # path('',views.demo,name='demo'),
    # path('add/',views.addition,name='addition'),
    # path('sub/',views.subtraction,name='subtraction')
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
