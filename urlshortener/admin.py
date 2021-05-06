from django.contrib import admin
from .models import UserUrl, BlockedDomain


class UserUrlAdmin(admin.ModelAdmin):
    fieldsets = [
        ('User input', {'fields': ['user_url', 'create_date']}),
        ('Resolve', {'fields': ['resolve_path', 'resolve_host', 'status', 'pub_date', 'user_domain']}),
        ('Block info', {'fields': ['block_reason', 'block_date']})
    ]
    readonly_fields = ('resolve_path', 'resolve_host', 'user_domain')
    # list
    list_display = ('user_url', 'short_url_no_schema', 'pub_date', 'is_active', 'is_blocked')
    search_fields = ('user_domain', 'user_url', )
    list_per_page = 100


class BlockedDomainAdmin(admin.ModelAdmin):
    # list
    list_display = ('pk', 'domain', 'block_date')
    list_display_links = ('pk',)
    list_editable = ('domain',)
    list_per_page = 100


# Register your models here.
admin.site.register(UserUrl, UserUrlAdmin)
admin.site.register(BlockedDomain, BlockedDomainAdmin)
