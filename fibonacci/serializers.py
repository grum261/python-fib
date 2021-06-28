import time

from rest_framework import serializers
from .models import FibonacciSequence, FibonacciSequenceTask
from fibonacci.tasks import fibonacci_seq
from django.utils import timezone
from celery import current_app
from django.http.response import JsonResponse


class FibonacciSequenceSerializer(serializers.ModelSerializer):
    taskID = serializers.CharField(read_only=True)
    n = serializers.IntegerField()
    startTime = serializers.DateTimeField(read_only=True)
    endTime = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)
    executionTime = serializers.TimeField(read_only=True)

    class Meta:
        model = FibonacciSequence
        fields = ('n', 'taskID', 'startTime', 'endTime', 'status', 'executionTime')

    def validate(self, attrs):
        if attrs['n'] < 0:
            raise serializers.ValidationError('Параметр не должен быть меньше нуля')

        return attrs

    def create(self, validated_data):
        start = timezone.now()
        task = fibonacci_seq.delay(validated_data['n'])
        while not task.ready():
            time.sleep(0.000001)

        FibonacciSequenceTask.objects.create(
            taskID=task.id, startTime=start, endTime=timezone.now(),
            n=validated_data['n'], status=task.status,
        )

        return FibonacciSequence.objects.create(sequence=task.get())
