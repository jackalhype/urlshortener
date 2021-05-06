from django.contrib import admin
from .models import UserUrl


class UserUrlAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User input', {'fields': ['user_url', 'create_date']}),
        ('Resolve', {'fields': ['resolve_path', 'resolve_host', 'status', 'pub_date', 'user_domain']}),
        ('Block info', {'fields': ['block_reason', 'block_date']})
    ]
    readonly_fields = ('resolve_path', 'resolve_host', 'user_domain')

    # list
    list_display = ('user_url', 'short_url_no_schema', 'pub_date')


# Register your models here.
admin.site.register(UserUrl, UserUrlAdmin)
