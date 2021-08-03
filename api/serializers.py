from rest_framework import serializers

from .models import Shop


class ShopSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        show = self.context['request'].GET.getlist('show')
        group = self.context['request'].GET.getlist('group')
        fields = None
        if group:
            fields = group
        if show:
            fields = show
        if show and group:
            fields = show+group
        if fields:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Shop
        fields = ('date', 'country', 'shop', 'visitors', 'earnings',)
