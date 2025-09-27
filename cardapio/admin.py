from django.contrib import admin
from .models import Proteina

@admin.register(Proteina)
class ProteinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'disponivel')
    list_filter = ('disponivel',)
    search_fields = ('nome',)
    
# Register your models here.
