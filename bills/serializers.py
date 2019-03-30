from rest_framework.serializers import ModelSerializer
from bills.models import Category, Bill


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BillSerializer(ModelSerializer):

    class Meta:
        model = Bill
        fields = '__all__'
