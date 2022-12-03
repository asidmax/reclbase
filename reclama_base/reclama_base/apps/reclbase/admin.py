from django.contrib import admin

from .models import Item, Location, Project, Reclamacia, ReclUser


class LocationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'vch_no', 'address',)
    list_display_links = ('vch_no',)
    search_fields = ('vch_no',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'item_no', 'item_frame', 'item_engine', 'item_tn_to', 'item_tn_from')
    list_display_links = ('item_type', 'item_no', 'item_frame')
    search_fields = ('item_type', 'item_no', 'item_frame')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'project_no', 'with_npo', 'with_mzkt')
    list_display_links = ('project_no',)
    search_fields = ('project_no',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'is_activated', 'date_joined')
    search_fields = ('first_name', 'last_name', 'username')
    fields = (('username', 'email'), ('first_name', 'last_name'), ('send_messages', 'is_active', 'is_activated'), ('is_staff', 'is_superuser'), 'groups', 'user_permissions', ('last_login', 'date_joined'))


admin.site.register(Project, ProjectAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ReclUser, UserAdmin)