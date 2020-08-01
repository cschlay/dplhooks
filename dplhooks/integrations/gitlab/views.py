from django.http import JsonResponse

from dplhooks.views import APIView


class DeployWebhook(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            'ok': 's'
        }, status=200)
