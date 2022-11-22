from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from apis.utils import ZeroClient, ZeroEndpoints


class NetworkAPIView(APIView):
    endpoint = ZeroEndpoints().network

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)

    def post(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.post(self.endpoint, data=request.data)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)


class NetworkDetailAPIView(APIView):
    endpoint = ZeroEndpoints().network_detail

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint.replace(":networkID", kwargs["networkID"]))
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)

    def post(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.post(self.endpoint.replace(":networkID", kwargs["networkID"]), data=request.data)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)

    def delete(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.delete(self.endpoint.replace(":networkID", kwargs["networkID"]))
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)
