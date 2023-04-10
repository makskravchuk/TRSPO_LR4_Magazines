from rest_framework import serializers

from magazines.models import Magazine


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = "__all__"
