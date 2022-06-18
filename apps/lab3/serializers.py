from rest_framework import serializers
from .models import UtilizationMachine, SamplesMachine, RevenueMachine, MissedRevenueMachine, statsMachine, monthlystatsMachine, UtilizationAssay, SamplesAssay, RevenueAssay, MissedRevenueAssay, statsAssay, monthlystatsAssay


class UtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilizationMachine
        fields = '__all__'


class SamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplesMachine
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueMachine
        fields = '__all__'


class MissedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissedRevenueMachine
        fields = '__all__'


class statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = statsMachine
        fields = '__all__'


class monthlystatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlystatsMachine
        fields = '__all__'

# assay 
class AssayUtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UtilizationAssay
        fields = '__all__'


class AssaySamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SamplesAssay
        fields = '__all__'


class AssayRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueAssay
        fields = '__all__'


class AssayMissedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissedRevenueAssay
        fields = '__all__'


class AssaystatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = statsAssay
        fields = '__all__'


class AssaymonthlystatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlystatsAssay
        fields = '__all__'
