from __future__ import unicode_literals

from django.db import models

class Grn(models.Model):
    doc_id = models.AutoField(primary_key=True)
    date = models.DateField()
    supplier_name = models.CharField(max_length=30) 
    received_by = models.CharField(max_length=30)
    

class Supply_voucher(models.Model):
    doc_id = models.AutoField(primary_key=True)
    date = models.DateField()
    issued_by = models.CharField(max_length=30)
    received_by = models.CharField(max_length=30)
    

class Item(models.Model):
    title = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    supply_voucher = models.ForeignKey(Supply_voucher, 
        on_delete=models.CASCADE,
        related_name='items',
        blank=True, 
        null=True)
    grn = models.ForeignKey(Grn, 
        on_delete=models.CASCADE,
        related_name='items',
        blank=True, 
        null=True)
    
    def value(self):
        return (self.quantity * self.price)