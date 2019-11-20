from .models import SystemMessage

def system_message_context_processor(req):
    return {'system_message': SystemMessage.objects.all().last()}