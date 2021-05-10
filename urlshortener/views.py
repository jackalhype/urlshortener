from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from urlshortener.models import UserUrl
from urllib.parse import urlsplit
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework.decorators import throttle_classes
from rest_framework.throttling import UserRateThrottle


def redirectView(request, resolve_path):
    """
    shortened url itself
    """
    user_url = get_object_or_404(UserUrl, resolve_path=resolve_path)
    redirect_url = user_url.user_url
    p = urlsplit(redirect_url)
    if not p.scheme:
        redirect_url = 'http://' + redirect_url
    return redirect(redirect_url)


class DayLimitUserUrlPostThrottle(UserRateThrottle):
    rate = '50/day'


class UserUrlApiView(APIView):
    @throttle_classes([DayLimitUserUrlPostThrottle])
    def post(self, request):
        req_ser = serializers.UserUrlPostSerializer(data=request.data)
        if not req_ser.is_valid():
            return Response({'errors': req_ser.errors}, status=status.HTTP_400_BAD_REQUEST)

        model, err = req_ser.create(req_ser.validated_data)
        if err:
            return Response({'errors': err}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        resp_ser = serializers.UserUrlSerializer(model)
        return Response({'data': resp_ser.data}, status=status.HTTP_201_CREATED)
