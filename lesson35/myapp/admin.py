from django.contrib import admin
from .models import Video, Author, Like, Comment, Category, Advertise

# Register your models here.


class VideoAdmin(admin.ModelAdmin):
    pass

class AuthorAdmin(admin.ModelAdmin):
    pass

class LikeAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class AdvertiseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Video)
admin.site.register(Author)
admin.site.register(Like)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Advertise)
