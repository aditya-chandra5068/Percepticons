from django.contrib import admin
from blog.models import Post, Topic
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/tinyInject.js',)


admin.site.register(Topic)
