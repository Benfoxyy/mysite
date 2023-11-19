from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    empty_value_display='-empty-'
    list_display=('title','status','created_date')
    search_fields=['title','content']