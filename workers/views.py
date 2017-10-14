from rest_framework import viewsets

from workers.models import Worker, WorkerType
from workers.serializers import WorkerSerializer, WorkerTypeSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows workers to be viewed or edited.
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows worker_types to be viewed or edited.
    """
    queryset = WorkerType.objects.all()
    serializer_class = WorkerTypeSerializer
