# Generated by Django 3.2.4 on 2021-06-27 17:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FibonacciSequence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequence', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), db_column='sequence', size=None)),
            ],
            options={
                'db_table': 'fibonacci_sequences',
            },
        ),
        migrations.CreateModel(
            name='FibonacciSequenceTask',
            fields=[
                ('taskID', models.CharField(db_column='task_id', max_length=255, primary_key=True, serialize=False)),
                ('n', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('startTime', models.DateTimeField(db_column='start_time')),
                ('endTime', models.DateTimeField(db_column='end_time')),
            ],
            options={
                'db_table': 'fibonacci_sequences_tasks',
            },
        ),
    ]