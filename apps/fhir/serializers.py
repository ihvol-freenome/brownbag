from rest_framework import serializers

class GenericModelSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
