from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response

from .serializers import FibonacciSequenceSerializer
from .models import FibonacciSequenceTask

from celery import current_app


class FibonacciSequenceCreateView(ListCreateAPIView):
    queryset = FibonacciSequenceTask.objects.all()
    serializer_class = FibonacciSequenceSerializer

    def get(self, request):
        query = FibonacciSequenceTask.objects.all().values()

        tasks = []
        for value in query:
            response = {}
            task = current_app.AsyncResult(value['taskID'])

            response['taskID'] = value['taskID']
            response['status'] = task.status
            response['startTime'] = value['startTime']
            response['endTime'] = value['endTime']
            response['executionTime'] = value['endTime'] - value['startTime']

            tasks.append(response)

        return Response(tasks)

    def post(self, request):
        serializer = FibonacciSequenceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()

        return Response({'id': saved.id})


class FibonacciTaskListView(ListAPIView):
    def get(self, request, taskID):
        try:
            query = FibonacciSequenceTask.objects.filter(taskID=taskID).values()[0]
        except IndexError:
            return Response({'error': 'Задачи с данным id не существует'})

        task = current_app.AsyncResult(taskID)

        response = {
            'taskID': task.id, 'taskStatus': task.status,
            'startTime': query['startTime'], 'endTime': query['endTime']
        }

        response['executionTime'] = response['endTime'] - response['startTime']

        if task.status == 'SUCCESS':
            response['result'] = task.result

        return Response(response)
