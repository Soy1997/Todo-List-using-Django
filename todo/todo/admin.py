from django.contrib import admin
from .models import Todoo

@admin.register(Todoo)
class TodooAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'user', 'created_at')
    list_filter = ('completed', 'user', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)