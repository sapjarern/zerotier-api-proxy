import os
import json
import base64
import logging
from datetime import datetime
from typing import Union

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from django.conf import settings
from rest_framework import status


class BaseClient:

    def __init__(self):
        self.session = Session()
        retry = Retry(connect=3, backoff_factor=0.5)
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount('http://', adapter)
        # self.session.mount('https://', adapter)

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        return response

    def post(self, url, data, **kwargs):
        response = self.session.post(url, data=json.dumps(data), **kwargs)
        return response

    def put(self, url, data, **kwargs):
        response = self.session.put(url, data=json.dumps(data), **kwargs)
        return response

    def patch(self, url, data, **kwargs):
        response = self.session.patch(url, data=json.dumps(data), **kwargs)
        return response

    def delete(self, url, **kwargs):
        response = self.session.delete(url, **kwargs)
        return response


class ZeroClient(BaseClient):
    headers = {
        "Content-Type": "application/json",
        "X-ZT1-Auth": "",
    }

    def __init__(self, *args, **kwargs):
        self.headers.update({"X-ZT1-Auth": settings.ZERO_TOKEN})
        super().__init__()

    def get(self, url, **kwargs):
        return super().get(url, headers=self.headers, **kwargs)

    def post(self, url, data, **kwargs):
        return super().post(url, data, headers=self.headers, **kwargs)

    def put(self, url, data, **kwargs):
        return super().put(url, data, headers=self.headers, **kwargs)

    def patch(self, url, data, **kwargs):
        return super().patch(url, data, headers=self.headers, **kwargs)

    def delete(self, url, **kwargs):
        return super().delete(url, headers=self.headers, **kwargs)


class ZeroEndpoints:
    _baseURL = settings.ZERO_URL
    _status = f"{_baseURL}/status"

    _network = f"{_baseURL}/network"
    _networkDetail = f"{_baseURL}/network/:networkID"

    _controller = f"{_baseURL}/controller"
    _controllerNetwork = f"{_baseURL}/controller/network"
    _controllerNetworkCreate = f"{_baseURL}/controller/network/:controllerID"
    _controllerNetworkDetail = f"{_baseURL}/controller/network/:networkID"
    _controllerNetworkDetailMember = f"{_baseURL}/controller/network/:networkID/member"

    _peer = f"{_baseURL}/peer"
    _peerDetail = f"{_baseURL}/peer/:address"

    @property
    def status(self):
        return self._status
    
    @property
    def network(self) -> str:
        return self._network

    @property
    def network_detail(self) -> str:
        return self._networkDetail

    @property
    def controller(self) -> str:
        return self._controller

    @property
    def controller_network(self) -> str:
        return self._controllerNetwork

    @property
    def controller_network_create(self) -> str:
        return self._controllerNetworkCreate

    @property
    def controller_network_detail(self) -> str:
        return self._controllerNetworkDetail

    @property
    def controller_network_member(self) -> str:
        return self._controllerNetworkDetailMember

    @property
    def peer(self) -> str:
        return self._peer

    @property
    def peer_detail(self) -> str:
        return self._peerDetail
