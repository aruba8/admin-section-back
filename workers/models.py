from django.db import models


class WorkerType(models.Model):
    worker_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.worker_type_name


class Worker(models.Model):
    worker_type = models.ForeignKey(WorkerType)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
