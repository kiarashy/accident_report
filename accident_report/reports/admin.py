from django.contrib import admin
from .models import AccidentReport

@admin.register(AccidentReport)
class AccidentReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'created_at')  # Show these fields
    search_fields = ('title', 'description', 'location')  # Add search bar
    list_filter = ('created_at',)  # Add filter options
    actions = ['delete_selected']  # ✅ Add bulk delete action

# Alternatively, just use:
# admin.site.register(AccidentReport)  # Without customization
