from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import UserUrl

class UserUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUrl
        fields = [
            'user_url',
            'create_date',
            'pub_date',
            'resolve_path',
            'resolve_host',
            'status',
            'block_reason',
            'block_date',
            'user_url_hash',
            'user_domain',
        ]

class UserUrlPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUrl
        fields = [
            'user_url',
        ]

    def create(self, validated_data, no_save=True, **kwargs):
        model = UserUrl(user_url=validated_data['user_url'])
        try:
            model.prepareForSave()
        except ValidationError as e:
            return (model, e)
        return (model, None)
