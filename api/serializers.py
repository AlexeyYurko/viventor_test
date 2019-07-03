from django.conf import settings
from rest_framework import exceptions, serializers
from rest_hooks.models import Hook

from contacts.models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date')


class HookSerializer(serializers.ModelSerializer):
    def validate_event(self, event):
        if event not in settings.HOOK_EVENTS:
            err_msg = "Unexpected event {}".format(event)
            raise exceptions.ValidationError(detail=err_msg, code=400)
        return event

    class Meta:
        model = Hook
        fields = '__all__'
        read_only_fields = ('id',)
