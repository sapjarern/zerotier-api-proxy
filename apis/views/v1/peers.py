from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from apis.utils import ZeroClient, ZeroEndpoints


class PeerAPIView(APIView):
    endpoint = ZeroEndpoints.peer

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)


class PeerDetailAPIView(APIView):
    endpoint = ZeroEndpoints.peer_detail

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint.replace(":address", kwargs["address"]))
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)
