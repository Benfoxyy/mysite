from django.contrib import admin
from blog.models import Post,category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','status','created_date')
    search_fields=['title','content']
    summernote_fields = ('content',)
admin.site.register(category)