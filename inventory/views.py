from django.shortcuts import render

from django.http import Http404
from django.http import HttpResponse


from inventory.models import Grn
from inventory.models import Supply_voucher
from inventory.models import Item

def grnz(request):
    return HttpResponse('<p> this is a grn list for old times sake! </p>')

def supply_voucherz(request):
    return HttpResponse('<p> this is a supply_voucherz list for old times sake! </p>')

def grn(request):
    grn = Grn.objects.all()
    return render(request, 'inventory/grn.html', {
        'grns' : grn,
    })
    

def grn_detail(request, id):
    try:
        grn = Grn.objects.get(doc_id=id)
        items_in_grn = grn.items.all()
    except Grn.DoesNotExist:
        raise Http404('This grn does not exist')
    return render(request, 'inventory/grn_detail.html', {
        'items_in_grn' : items_in_grn,
    })
    
def supply_voucher(request):
    supply_voucher = Supply_voucher.objects.all()
    return render(request, 'inventory/supply_voucher.html', {
        'supply_vouchers' : supply_voucher,
    })
    

def supply_voucher_detail(request, id):
    try:
        supply_voucher = Supply_voucher.objects.get(doc_id=id)
    except Supply_voucher.DoesNotExist:
        raise Http404('This supply_voucher does not exist')
    return render(request, 'inventory/supply_voucher_detail.html', {
        'supply_voucher' : supply_voucher,
    })



