from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from app_user.models import UserModel
from app_user.serializers import UserSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
# Create your views here.

class UserView(ViewSet):
    # @swagger_auto_schema(responses=UserSerializer)
    def list(self, request):
        queryset = UserModel.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=UserSerializer)
    def create(self, request):
        serialized_obj = UserSerializer(data=request.data)
        if serialized_obj.is_valid(raise_exception=True):
            serialized_obj.save()
        return Response("User Created")

    def retrieve(self, request, pk=None):
        queryset = UserModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


    def destroy(self, request, pk=None):
        queryset = UserModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        return Response("User Deleted")