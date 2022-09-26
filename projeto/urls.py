from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('',views.home),
    path('posts/<int:post_id>',views.post),
    path('manchetes/<int:manchete_id>',views.manchete),
    path('welcomes/<int:welcome_id>',views.welcome),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
