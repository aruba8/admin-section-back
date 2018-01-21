from rest_framework import serializers

from workers.models import Worker, WorkerType


class WorkerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerType
        fields = '__all__'


class WorkerSerializer(serializers.ModelSerializer):
    worker_type = WorkerTypeSerializer(read_only=False)

    class Meta:
        model = Worker
        fields = '__all__'

    def update(self, instance, validated_data):
        worker_type_data = validated_data.pop('worker_type')
        worker_type = WorkerType.objects.get(**worker_type_data)
        instance.name = validated_data['name']
        instance.worker_type = worker_type
        instance.save()
        return instance

    def create(self, validated_data):
        name = validated_data.pop('name')
        worker_type_data = validated_data.pop('worker_type')
        worker_type = WorkerType.objects.get(**worker_type_data)
        worker = Worker.objects.create(name=name, worker_type=worker_type)
        return worker
