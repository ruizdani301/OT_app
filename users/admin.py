from django.contrib import admin
"""
from users.models import User, Ot


class UserInline(admin.TabularInline):
    model = User

class UserAdmin(admin.ModelAdmin):
    list_display=('id_user', 'name', 'last_name', 'job')
    inlines = (UserInline,)

class OtAdmin(admin.ModelAdmin):
    list_display=('cod_sap', 'description', 'location')

admin.site.register(User, UserAdmin)
admin.site.register(Ot, OtAdmin)
"""