
import time
import hashlib

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ShortenerSerializer
from .models import Shortener

# Shortener Viewset

class ShortenerViewSet(viewsets.ModelViewSet):
    permission_classes = [
    ]
    serializer_class = ShortenerSerializer

    def get_queryset(self):
        return None

    def perform_create(self, serializer):

        def QRcode(QRdata):
            QRobject = QRCode(QRdata, encoding='utf-8')
            qrName = "QR_{}.svg".format(hashlib.sha224(bytes("{} - {}".format(QRdata, time.time()), 'utf-8')).hexdigest())
            QRobject.svg("media/{}".format(qrName), scale = 3)
            return qrName

        #check slug
        slug = self.request.data['slug']

        serializer.save(
            responseURL = slug
        )

