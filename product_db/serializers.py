from rest_framework import serializers
from .models import *
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('product_id','product_name','stock_qty')
class supplierSerializerModel(serializers.ModelSerializer):
    class Meta:
        model=supplier
        fields=('supplier_id','supplier_name','supplier_address')

# Created nested serializer to return purchase order annd suppplier
class purchaseOrderSerializer(serializers.ModelSerializer):
    supplier_id = supplierSerializerModel()
    class Meta:
        model= purchase_order
        fields=('purchase_order_id','supplier_id','date_created',)
    def create(self, validated_data):
        supplier_data=validated_data.pop('supplier_id')
        supplierEx = supplier.objects.create(**supplier_data)
        purchase_order = User.object.create(supplier_id=supplier,**validated_data)
        return purchase_order
    