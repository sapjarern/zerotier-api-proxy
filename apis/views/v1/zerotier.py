
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apis.utils import ZeroClient, ZeroEndpoints


class NodeStatusAPIView(APIView):

    def get(self, request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(ZeroEndpoints().status)
        if response.status_code >= status.HTTP_300_MULTIPLE_CHOICES:
            return Response(data=response.content, status=response.status_code)

        return Response(data=response.json(), status=response.status_code)

