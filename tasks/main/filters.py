import django_filters
from .models import Task

class CustomDescriptionFilter(django_filters.CharFilter):
    def filter(self, queryset, value):
        if value:
            return queryset.filter(description__icontains=value)
        return queryset

class TaskFilter(django_filters.FilterSet):
    description = CustomDescriptionFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['name', 'assigned_user', 'status', 'description']
