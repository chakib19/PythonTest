
from rest_framework import serializers
from todo.models import TodoItem

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
  url = serializers.ReadOnlyField()
  class Meta:
    mode1 = TodoItem
    fields = ('url', 'title', 'completed', 'order')
