import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from api.serializers import ContactSerializer
from contacts.models import Contact
from . import hookevents as webhook_events


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer


@require_POST
@csrf_exempt
def webhook(request):
    data = json.loads(request.body)
    process_webhook(data)
    return HttpResponse(status=200)


def process_webhook(event):
    event_name = event['event']

    function_name = event_name.replace('.', '_')
    function = getattr(webhook_events, function_name, None)

    if function:
        function(event)
    else:
        print('Event %s is not registered.' % event_name)
