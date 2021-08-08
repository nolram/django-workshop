from django.contrib import admin
from .models import PrizeDraw, Winner

class PrizeDrawAdmin(admin.ModelAdmin):
    pass

class WinnerAdmin(admin.ModelAdmin):
    pass

admin.site.register(PrizeDraw, PrizeDrawAdmin)
admin.site.register(Winner, WinnerAdmin)
