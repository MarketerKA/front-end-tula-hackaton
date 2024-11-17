from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Bid, Worker

# Register Worker model
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)  # Fields to display in the list view
    search_fields = ('user__username',)  # Enable searching by username

# Register Bid model
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', "username", 'type', 'coordinates', 'status', 'created_at',  'assigned_worker')
    list_filter = ('status', 'type', 'created_at')  # Add filters for status, type, and date
    search_fields = ('address', 'description', 'user__username')  # Enable search by relevant fields
    ordering = ('-created_at',)  # Order by creation date descending
    readonly_fields = ['created_at']  # Make certain fields read-only

# Extend the User admin to include Worker inline
class WorkerInline(admin.StackedInline):
    model = Worker
    can_delete = False
    verbose_name_plural = 'Worker Profiles'

class CustomUserAdmin(UserAdmin):
    inlines = [WorkerInline]  # Add inline editing for Worker profile

# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
