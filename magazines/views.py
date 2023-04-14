from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from magazines.models import Magazine
from magazines.permissions import IsAdminPermission
from magazines.serializers import MagazineSerializer


# Create your views here.
class MagazineListAPIView(ListAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializer

    @method_decorator(cache_page(60))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class MagazineAPIView(APIView):
    def get_permissions(self):
        if self.request.method == 'POST' or self.request.method == "PUT" or self.request.method == "DELETE":
            return [IsAdminPermission()]
        return [AllowAny()]

    @method_decorator(cache_page(60))
    def get(self, request, pk):
        magazine = Magazine.objects.get(pk=pk)
        serializer = MagazineSerializer(magazine)
        return Response(data=serializer.data)

    def post(self, request):
        magazine = MagazineSerializer(data=request.data)
        if magazine.is_valid(raise_exception=True):
            magazine.save()
        return Response(status=201)

    def put(self, request, pk):
        try:
            instance = Magazine.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        serializer = MagazineSerializer(data=request.data, instance=instance)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({"magazine": serializer.data})

    def delete(self, request, pk):
        try:
            Magazine.objects.filter(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})
        return Response(status=200)
