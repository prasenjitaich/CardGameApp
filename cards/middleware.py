from django.http import JsonResponse
from rest_framework import status


class ExceptionHandlingMiddleware:
    """
        Class is used for Handling the Exception.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        return JsonResponse({'status': 0,
                             'message': str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
