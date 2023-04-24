from collections import OrderedDict
from rest_framework import serializers
from cars.models import Waybill, Engine, Passport, Distribution, Car


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = '__all__'


class WaybillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        fields = '__all__'


class DistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distribution
        fields = '__all__'


class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = '__all__'


class CarCreateUpdateSerializer(serializers.ModelSerializer):
    engine = EngineSerializer()
    distribution = DistributionSerializer()
    passport = PassportSerializer()
    waybill = WaybillSerializer()

    def create(self, validated_data: dict):
        nested_fields = {}
        for field, data in validated_data.items():
            if isinstance(data, OrderedDict):
                nested_fields[field] = (
                    self.fields[field].Meta.model.objects.create(**data)
                )
        validated_data.update(nested_fields)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        nested_fields = {}
        for field, value in validated_data.items():
            if isinstance(value, OrderedDict):
                obj = getattr(instance, field)
                for obj_attr, obj_value in value.items():
                    setattr(obj, obj_attr, obj_value)
                obj.save()
                value = obj

            nested_fields[field] = value
        validated_data.update(nested_fields)
        return super().update(instance, validated_data)

    class Meta:
        model = Car
        fields = '__all__'


class CarListSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.name", allow_null=True)
    group = serializers.CharField(source='group.name', allow_null=True)

    class Meta:
        model = Car
        fields = (
            'id',
            'inventory_number',
            'brand',
            'year',
            'gov_number',
            'group'
        )


class CarDisplaySerializer(CarCreateUpdateSerializer, CarListSerializer):
    type = serializers.CharField(
        source='type.name', allow_null=True
    )
    manufacturer = serializers.CharField(
        source='manufacturer.name', allow_null=True
    )
    body = serializers.CharField(
        source="body.name", allow_null=True
    )
    car_class = serializers.CharField(
        source="car_class.name", allow_null=True
    )
    color = serializers.CharField(
        source="color.name", allow_null=True
    )
    service = serializers.CharField(
        source="service.name", allow_null=True
    )
    subdivision = serializers.CharField(
        source="subdivision.name", allow_null=True
    )
    source = serializers.CharField(
        source="source.name", allow_null=True
    )
    warehouse = serializers.CharField(
        source="warehouse.name", allow_null=True
    )
    gasoline_brand = serializers.CharField(
        source="gasoline_brand.name", allow_null=True
    )

    class Meta:
        model = Car
        fields = '__all__'