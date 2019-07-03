from rest_framework import viewsets
from rest_hooks.models import Hook

from api.serializers import ContactSerializer, HookSerializer
from contacts.models import Contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer


class HookViewSet(viewsets.ModelViewSet):
    queryset = Hook.objects.all()
    model = Hook
    serializer_class = HookSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
