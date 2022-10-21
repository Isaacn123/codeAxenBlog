from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on','status')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    list_filter = ['created_on']


admin.site.register(Post, PostAdmin)