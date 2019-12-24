from django.shortcuts import render

# Create your views here.


from quickstart.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-created')
    serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     允许组查看或编辑的API路径。
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
