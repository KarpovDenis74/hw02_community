from django.contrib import admin
# из файла models импортируем модель Post
from .models import Post, Group

class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug") 
    search_fields = ("title",) 
    list_filter = ("slug",) 
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author") 
    search_fields = ("text",) 
    list_filter = ("pub_date",) 
    empty_value_display = "-пусто-" # это свойство сработает для всех колонок: где пусто - там будет эта строка



# при регистрации модели Post источником конфигурации для неё назначаем класс PostAdmin
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)


