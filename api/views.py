from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your views here.
class UserList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
class GetToken(APIView):
    def post(self, request):
        password = request.data.get('password')
        username = request.data.get('username')
        user = User.objects.get(username=username)
        if user.check_password(password):
            token,_ = Token.objects.get_or_create(user=user)
            content = {'token': token.key}
        return Response(content)