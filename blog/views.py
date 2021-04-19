from django.shortcuts import render
from .models import blog,comment
from .serializers import blogserializer,commentserializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class postlist(generics.RerieveUpdatedDestroyApiView):
    queryset=blog.objects.prefetch_related('comment').all()
    serializer_class=blogserializer
    permission_class=[permissions.IsAuthenticated]
