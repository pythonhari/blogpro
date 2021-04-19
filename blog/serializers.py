from .models import blog,comment
from rest_framework.serializers import ModelSerializer

class blogserializer(ModelSerializer):
    comments=serializers.HyperLinkeddRelatedField(many=True,read_only=True)
    class Meta:
        model=blog
        fields='__all__'
class commentserializer(ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'
