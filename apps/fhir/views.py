from django.apps import apps
from rest_framework import viewsets

from .serializers import GenericModelSerializer
import django_filters.rest_framework


class FHIRModelView(viewsets.ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ('id', 'status')

    def get_queryset(self):
        model = self.get_model(self.kwargs.get("model"))
        return model.objects.all()

    def get_serializer_class(self):
        model = self.get_model(self.kwargs.get("model"))
        GenericModelSerializer.Meta.model = model
        return GenericModelSerializer

    def get_model(self, name):
        return apps.get_model(app_label='fhir', model_name=name)
