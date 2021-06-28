from django.utils.timezone import now
from django.db import models
from django.contrib.postgres.fields import ArrayField


class FibonacciSequence(models.Model):
    # INSERT INTO fibonacci_n (fib_value) (SELECT unnest(array[0, 1, 1, 2, 3, 5, 8]))
    # и потом просто делать селект по id (который равен n), если n больше, чем последнее id
    # в базе, то делаем селект до последнего значения, остальное досчитываем, отдаем и пишем в базу
    sequence = ArrayField(models.TextField(), db_column='sequence')

    class Meta:
        db_table = 'fibonacci_sequences'


class FibonacciSequenceTask(models.Model):
    taskID = models.CharField(db_column='task_id', max_length=255, primary_key=True)
    n = models.IntegerField()
    status = models.CharField(max_length=255)
    startTime = models.DateTimeField(db_column='start_time')
    endTime = models.DateTimeField(db_column='end_time')

    class Meta:
        db_table = 'fibonacci_sequences_tasks'
