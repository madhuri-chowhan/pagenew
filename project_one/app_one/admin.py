from django.contrib import admin
from app_one.models import Topic, web,AccessRecord

# Register your models here.
admin.site.register(Topic)
admin.site.register(web)
admin.site.register(AccessRecord)