from rest_framework import serializers

from workers.models import Worker, WorkerType


class WorkerSerializer(serializers.ModelSerializer):
    worker_type = serializers.SlugRelatedField(slug_field='worker_type_name', read_only=True)

    class Meta:
        model = Worker
        fields = '__all__'


class WorkerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerType
        fields = '__all__'
