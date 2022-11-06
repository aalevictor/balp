import hashlib
import json

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
# from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import User

from .tokens import account_activation_token


# Create your views here.
def get_request_data(self, request):
    try:
        o = request.body.decode('utf-8')
        request_data = json.loads(o)
    except:
        request_data = request.data
    return request_data

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('https://ariedoverse.herokuapp.com/login?activate=true')
    else:
        return False

def activateEmail(request, user, to_email):
    try:
        mail_subject = 'Entre para a tropa do Calvo'

        username = user.twitch,
        domain = get_current_site(request).domain
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = account_activation_token.make_token(user)
        protocol = 'https' if request.is_secure() else 'http'

        message2 = "Ei, {}! Ative agora mesmo sua conta, é só clicar no link {}://{}/activate/{}/{}".format(username, protocol, domain, uid, token)
        email = EmailMessage(mail_subject, message2, to=[to_email])

        if email.send():
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
        pass

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
                user.is_active = False
                user.save()
                if user.id:
                    act = activateEmail(request, user, data['email'])
                    if act:
                        st = status.HTTP_201_CREATED
                        error = 'Usuário criado!'
                    else:
                        user.delete()
                        st = status.HTTP_400_BAD_REQUEST
                        error = 'Verifique seu email e tente novamente'
        except Exception as e:
            error.append(str(e))

        response = dict(
            result=error
        )

        return Response(response, st)
