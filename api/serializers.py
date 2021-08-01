from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(ShopSerializer, self).__init__(*args, **kwargs)
        show = dict(self.context['request'].GET).get('show')
        group = dict(self.context['request'].GET).get('group')
        fields = None
        if show and group:
            fields = show+group
        elif show:
            fields = show
        elif group:
            fields = group
        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Shop
        fields = ('date', 'country', 'shop', 'visitors', 'earnings',)
