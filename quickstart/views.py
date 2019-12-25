from django.shortcuts import render

# Create your views here.


from quickstart.models import User, Test
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, TestSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
