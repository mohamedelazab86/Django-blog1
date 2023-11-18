from django.contrib import admin
from .models import Post,Category


# cust admin panel
class Postadmin(admin.ModelAdmin):
    list_display=['title','draft','publish_date','author']
    list_filter=['title','author']
    search_fields=['title','publish_date']
# Register your models here.
admin.site.register(Post,Postadmin)
admin.site.register(Category)
