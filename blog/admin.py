from django.contrib import admin
from blog.models import Post,category,Comments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','status','created_date')
    search_fields=['title','content']
    summernote_fields = ('content',)

@admin.register(category)
class categoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comments)
class commentsAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('name','approved','created_date')
    search_fields=['name','message']
    summernote_fields = ('content',)
