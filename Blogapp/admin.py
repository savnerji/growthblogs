from django.contrib import admin
from .models import CustomUser,Category,Post



class CategoryAdmin(admin.ModelAdmin):
    list_display=['category']

class PostAdmin(admin.ModelAdmin):
    list_display=['heading','body','category','thumb_url']





admin.site.register(CustomUser)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)


