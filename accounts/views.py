import hashlib
import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User


# Create your views here.
def get_request_data(self, request):
        try:
            o = request.body.decode('utf-8')
            request_data = json.loads(o)
        except:
            request_data = request.data
        return request_data
        
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
                md5_password = hashlib.md5(data['password'].encode('UTF-8')).hexdigest()
                user.password = md5_password
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

# class TwitchToken(APIView):
#     def get(self):
        
