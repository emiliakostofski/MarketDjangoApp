from django.contrib import admin
from .models import Vraboten, Kontakt_Informacii, Proizvod, Market, MarketVraboten, MarketProizvod

# Register your models here.

class MarketProizvodInline(admin.TabularInline):
    model = MarketProizvod
    extra = 0

class MarketAdmin(admin.ModelAdmin):
    list_display = ("ime", "kontakt_informacii",)
    inlines = [MarketProizvodInline,]
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MarketAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class ProizvodAdmin(admin.ModelAdmin):
    list_display = ("ime_proizvod", "kod",)
    list_filter = ("vid", "domashen",)


class VrabotenAdmin(admin.ModelAdmin):
    model = Vraboten
    list_display = ("ime_vraboten", "prezime_vraboten",)
    exclude = ("user",)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(VrabotenAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Proizvod, ProizvodAdmin)
admin.site.register(Vraboten, VrabotenAdmin)
admin.site.register(Market, MarketAdmin)
admin.site.register(Kontakt_Informacii)


