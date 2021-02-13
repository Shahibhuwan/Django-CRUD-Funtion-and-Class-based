from rest_framework import serializers
from .models import Task
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields ='__all__'



#this is like model.forms but we can also use this as formAPI