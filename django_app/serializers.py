from rest_framework import serializers
from .models import *

class PersonDetails(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields="__all__"

# class EmployeeDetails(serializers.ModelSerializer):
#     # url = serializers.HyperlinkedIdentityField(view_name="details-detail")
#     emp_id=EmployeeId(many=True)
#     class Meta:
#         model = Details
#         fields = ('emp_unique','emp_name','DOJ','emp_photo','emp_id')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

# class MenuSerializer(serializers.ModelSerializer):
#     # url = serializers.HyperlinkedIdentityField(view_name='item-detail',lookup_field='pk')
#     Menus = ItemSerializer(many=True, read_only=True)
#     class Meta:
#         model=Menu
#         fields=('name','age','Menus')


class MenuSerializer(serializers.ModelSerializer):
    Menus = serializers.StringRelatedField(many=True)   #many=True should be there
    class Meta:
        model=Menu
        fields=('name','age','Menus')



