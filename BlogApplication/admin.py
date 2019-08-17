from django.contrib import admin
from BlogApplication.models import Post,Category,Page
# Register your models here.

class Blog(admin.ModelAdmin):
    list_display = ('title','seo_url','time','category_list','is_active')
    search_fields = ('title', 'content','is_active')
    list_editable = ('category_list', 'is_active','time')
    list_filter = (
        ('is_active', admin.BooleanFieldListFilter),
    )


admin.site.register(Post,Blog)
admin.site.register(Category)
admin.site.register(Page)
