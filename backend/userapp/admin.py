from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Research_Interest)
admin.site.register(Publication)
admin.site.register(Tag)
admin.site.register(Location)
