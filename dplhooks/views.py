from django.views.generic.base import View


class APIView(View):
    def delete(self, request, *args, **kwargs):
        raise NotImplementedError

    def get(self, request, *args, **kwargs):
        raise NotImplementedError

    def post(self, request, *args, **kwargs):
        raise NotImplementedError

    def put(self, request, *args, **kwargs):
        raise NotImplementedError
