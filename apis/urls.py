from django.urls import path, include

from apis.views.v1 import zerotier, networks, peers, controllers

api_v1_urls = (
    [
        path('status/', zerotier.NodeStatusAPIView.as_view(), name='status'),

        path('network/', networks.NetworkAPIView.as_view(), name='network'),
        path('network/<str:networkID>', networks.NetworkDetailAPIView.as_view(), name='network-detail'),

        path('peer/', peers.PeerAPIView.as_view(), name='peer'),
        path('peer/<str:address>', peers.PeerDetailAPIView.as_view(), name='peer-detail'),

        path('controller/', controllers.ControllerAPIView.as_view(), name='controller'),
        path('controller/network/', controllers.ControllerNetworkAPIView.as_view(), name='controller-network'),
        path('controller/network/<str:networkID>/', controllers.ControllerNetworkDetailAPIView.as_view(), name='controller-network-detail'),
        path('controller/network/<str:networkID>/member/', controllers.ControllerNetworkMemberAPIView.as_view(), name='controller-network-member'),
    ],
    'api_v1')

urlpatterns = [
    path('v1/', include(api_v1_urls))
]
