from django.contrib import admin


# Register your models here.
from ATGApp.models import UserProfile, Stadium, Review


class StadiumAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name', )}


admin.site.register(UserProfile)
admin.site.register(Review)
admin.site.register(Stadium, StadiumAdmin)


