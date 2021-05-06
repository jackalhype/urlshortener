from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from urlshortener.models import UserUrl
from urllib.parse import urlsplit


def redirectView(request, resolve_path):
    user_url = get_object_or_404(UserUrl, resolve_path=resolve_path)
    redirect_url = user_url.user_url
    p = urlsplit(redirect_url)
    if not p.scheme:
        redirect_url = 'http://' + redirect_url
    return redirect(redirect_url)
