from django.http import JsonResponse

from dplhooks import settings


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        is_private = not request.path.startswith('/p')
        if is_private and ('AUTHORIZATION' not in request.META or request.META['AUTHORIZATION'] != settings.API_BEARER):
            return JsonResponse(data={'details': 'Need authorization.'}, status=401)
        return self.get_response(request)
