from django.http import HttpResponse


def index(request):
    return HttpResponse(
        'Hello world from Django! This is Shahron Buddy!!!\n',
        content_type='text/plain'
    )

