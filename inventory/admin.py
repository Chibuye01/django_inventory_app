from django.contrib import admin

from .models import Grn, Supply_voucher, Item

class ItemTabularInline(admin.TabularInline):
    list_display = ["title", "quantity", "price"]
    model = Item
       
class GrnAdmin(admin.ModelAdmin):
    list_display = ["doc_id", "date", "supplier_name", "received_by"]
    inlines = [ItemTabularInline]
    class Meta:
        model = Grn

class Supply_voucherAdmin(admin.ModelAdmin):
    list_display = ["doc_id", "date", "issued_by", "received_by"]
    inlines = [ItemTabularInline]
    class Meta:
        model = Supply_voucher
       
admin.site.register(Grn, GrnAdmin)
admin.site.register(Supply_voucher, Supply_voucherAdmin)
