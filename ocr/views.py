
import os
import uuid

import cv2
import pytesseract
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ocr.models import Image


# Create your views here.
class PerksAPI(APIView):
    def post(self, request):
        response = []
        file_obj = []
        st = status.HTTP_500_INTERNAL_SERVER_ERROR

        if request.FILES:
            st = status.HTTP_200_OK
            perks = [ 'C# DE NITRO', 'TROCA-TROCA', 'TRATAMENTO PRECOCE', 'CAI NUNCA', 'RATO DE ACADEMIA', 'DUAS SANFONADAS', 'DEIXA QUE EU COBRO', 'PITBULL', 'OPORTUNISTA', 'OLHA O LADRÃO', 'CABEÇA FRIA', 'CORAÇÃO QUENTE', 'NÃO VALE BOMBA', 'SÓ VALE DE LONGE', 'TIK-TOKA', 'COLA NO PÉ', 'DRIBLE DEVERIA VALER PA', 'PETER CROUCH DA SHOPEE', 'CUCABOL', 'COACHING QUÂNTICO', 'REI DO CHUTÃO', 'EDERSON DO ALIEXPRESS', 'COMO UM GATO', 'BEM POSICIONADO', 'MÃO FIRME', 'PONTOS ESCONDIDOS', 'CLUTCHZEIRO', 'INABALÁVEL', 'JOELHO DE AÇO', 'PONTOS LIVRES' ]
            matches = []

            file_obj = request.FILES['file']
            name, extension = os.path.splitext(file_obj.name)
            name = name.replace(" ", "_")

            image = Image()
            image.name = name
            unique = uuid.uuid4().hex

            fss = FileSystemStorage()
            fss.save('images/{}_{}{}'.format(name, unique, extension), file_obj)
            image.name = name
            image.url = 'media/images/{}_{}{}'.format(name, unique, extension)

            image.save()

            img = cv2.imread(str(image.url))
            predicted_result = pytesseract.image_to_string(img, lang='eng', config='--oem 3 --psm 1 -c tessedit_char_whitelist="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÇÃ#ÓÉ-ÂÁ0123456789 "')
            
            matches = [x for x in perks if x in predicted_result]

            response = dict(
                result = matches
            )    
        else:
            st = status.HTTP_400_BAD_REQUEST

        return Response(response, st)
