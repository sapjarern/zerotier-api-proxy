from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

from apis.utils import ZeroClient, ZeroEndpoints


class ControllerAPIView(APIView):
    endpoint = ZeroEndpoints().controller

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)


class ControllerNetworkAPIView(APIView):
    endpoint = ZeroEndpoints().controller_network

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)

    def post(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        if controller_id := request.data.get("controller_id", None):
            response = client.post(ZeroEndpoints().controller_network_create.replace(":controllerID", controller_id),
                                   request.data)
            return Response(
                data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
                status=response.status_code)
        else:
            return Response({"message": "controller_id is require."}, status=status.HTTP_400_BAD_REQUEST)


class ControllerNetworkDetailAPIView(APIView):
    endpoint = ZeroEndpoints().controller_network_detail

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


class ControllerNetworkMemberAPIView(APIView):
    endpoint = ZeroEndpoints().controller_network_member

    def get(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.get(self.endpoint.replace(":networkID", kwargs["networkID"]))
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)


class ControllerNetworkMemberDetailAPIView(APIView):
    endpoint = ZeroEndpoints().controller_network_member_detail

    def post(self, request: Request, *args, **kwargs):
        client = ZeroClient()
        response = client.post(self.endpoint
                               .replace(":networkID", kwargs["networkID"])
                               .replace(":memberID", kwargs["memberID"]), data=request.data)
        return Response(
            data=response.json() if response.status_code < status.HTTP_300_MULTIPLE_CHOICES else response.content,
            status=response.status_code)
