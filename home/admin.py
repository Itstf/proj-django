from django.contrib import admin
from home.models import Post, Welcome
from home.models import Manchete

# Register your models here.
admin.site.register(Post)
admin.site.register(Manchete)
admin.site.register(Welcome)