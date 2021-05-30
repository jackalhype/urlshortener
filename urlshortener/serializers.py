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
            'short_url_http',
            'short_url_https',
            'short_url_no_schema',
        ]

class UserUrlPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserUrl
        fields = [
            'user_url',
        ]

    def create(self, validated_data, no_save=False, **kwargs):
        model = UserUrl(user_url=validated_data['user_url'])
        try:
            model.prepareForSave()
        except ValidationError as e:
            models = UserUrl.objects.filter(user_url_hash=model.user_url_hash)
            if models.count() > 0:
                model = models[0]
                return (model, None)
            else:
                return (model, e)
        model.save()
        return (model, None)
