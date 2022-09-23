from django.contrib import admin
from .models import Gallery, News, Place, Culture
# Register your models here.

admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(Place)
admin.site.register(Culture)