from rest_framework import serializers
from .models import Tshirt, Order


class TshirtSerializer(serializers.ModelSerializer):

    class Meta:

        model = Tshirt

        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order

        fields = '__all__'