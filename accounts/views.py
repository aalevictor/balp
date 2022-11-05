import hashlib
import json

# from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import User


# Create your views here.
def get_request_data(self, request):
        try:
            o = request.body.decode('utf-8')
            request_data = json.loads(o)
        except:
            request_data = request.data
        return request_data

class VerifyUsers(APIView):

    def get(self, request):
        status = True
        
        twitch = self.request.GET.get('twitch', None)
        email = self.request.GET.get('email', None)
        discord = self.request.GET.get('discord', None)

        users = User.objects
        if twitch != None:
            users = users.filter(twitch=twitch)
        if email != None:
            users = users.filter(email=email)
        if discord != None:
            users = users.filter(discord=discord.replace('@', '#'))
        users = users.all()

        if len(users) > 0:
            status = False

        response = dict(
            available=status
        )

        return Response(response)

class CheckLogin(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):

        response = dict(
            twitch=request.user.twitch,
            email=request.user.email
        )

        return Response(response)
class UsersAPI(APIView):

    def post(self, request):
        st = status.HTTP_500_INTERNAL_SERVER_ERROR
        error = []

        data = get_request_data(self, request)

        user = User()

        try:
            if 'name' in data:
                user.name = data['name']
            else:
                error.append('O campo nome é obrigatório.')

            if 'password' in data:
                user.set_password(data['password'])
            else:
                error.append('O campo senha é obrigatório.')
                  
            if 'twitch' in data:
                twitch = data['twitch']
                aux = User.objects.filter(twitch=twitch).first()
                if not aux:
                    user.twitch = twitch
                else:
                    error.append('Login já utilizado.')
            else:
                error.append('O campo login é obrigatório.')

            if 'email' in data:
                user.email = User.objects.normalize_email(data['email'])
            else:
                error.append('O campo email é obrigatório.')

            if 'discord' in data:
                user.discord = data['discord']

            if len(error) == 0:
                user.save()
                if user.id:
                    st = status.HTTP_201_CREATED
                    error = 'Usuário criado!'
        except Exception as e:
            error.append(str(e))

        response = dict(
            result=error
        )

        return Response(response, st)
