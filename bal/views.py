import csv
import json
import locale
from datetime import datetime

from django.core.files.storage import FileSystemStorage
from googletrans import Translator
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

locale.setlocale(locale.LC_ALL, '')
translator = Translator()

from bal.models import Bal, Club, Goalkeeper, Player, Technical


# Create your views here.
def get_request_data(request):
        try:
            o = request.body.decode('utf-8')
            request_data = json.loads(o)
        except:
            request_data = request.data
        return request_data

def convertData(data, bal=Bal.objects.first()):
    updated = 0
    newRecords = 0
    errors=[]

    try:
        data['uniqueID']
        aux = []
        aux.append(data)
        data = aux
    except Exception as e:
        pass

    for player in data:
        new = False
        try:
            if 'uniqueID' in player:
                uniqueID = player['uniqueID']
                p = Player.objects.filter(uniqueID=uniqueID).first()

                if not p:
                    new = True
                    p = Player()
                    p.uniqueID = uniqueID
                    p.bal = bal

                cl = player['club'] if 'club' in player else 'Livre'
                club = Club.objects.filter(name=cl).first()
                if not club:
                    club = Club()
                    club.name = cl
                    club.save()

                p.club              = club
                p.name              = player['name']                if 'name'               in player else p.name              if p.name              else 'John Doe'
                p.nickname          = player['nickname']            if 'nickname'           in player else p.nickname          if p.nickname          else None
                p.birthDate         = player['birthDate']           if 'birthDate'          in player else p.birthDate         if p.birthDate         else datetime.now()
                p.age               = player['age']                 if 'age'                in player else p.age               if p.age               else 15
                p.nationality       = player['nationality']         if 'nationality'        in player else p.nationality       if p.nationality       else 'BRA'
                p.secondNationality = player['secondNationality']   if 'secondNationality'  in player else p.secondNationality if p.secondNationality else None
                p.height            = player['height']              if 'height'             in player else p.height            if p.height            else 150
                p.weight            = player['weight']              if 'weight'             in player else p.weight            if p.weight            else 55
                p.wage              = int(player['wage'])           if 'wage'               in player else p.wage              if p.wage              else 100
                p.contractEnd       = player['contractEnd']         if 'contractEnd'        in player else p.contractEnd       if p.contractEnd       else datetime.now()
                p.pressDescription  = player['pressDescription']    if 'pressDescription'   in player else p.pressDescription  if p.pressDescription  else 'Médio'
                p.personality       = player['personality']         if 'personality'        in player else p.personality       if p.personality       else 'Equilibrado'
                p.rightFoot         = player['rightFoot']           if 'rightFoot'          in player else p.rightFoot         if p.rightFoot         else 'Muito Forte'
                p.leftFoot          = player['leftFoot']            if 'leftFoot'           in player else p.leftFoot           if p.leftFoot         else 'Muito Fraco'
                p.position          = player['position']            if 'position'           in player else p.position          if p.position          else 'M (C)'
                p.currentAbility    = player['currentAbility']      if 'currentAbility'     in player else p.currentAbility    if p.currentAbility    else 1
                p.potentialAbility  = player['potentialAbility']    if 'potentialAbility'   in player else p.potentialAbility  if p.potentialAbility  else 1
                p.adaptability      = player['adaptability']        if 'adaptability'       in player else p.adaptability      if p.adaptability      else 1
                p.ambition          = player['ambition']            if 'ambition'           in player else p.ambition          if p.ambition          else 1
                p.consistency       = player['consistency']         if 'consistency'        in player else p.consistency       if p.consistency       else 1
                p.controversy       = player['controversy']         if 'controversy'        in player else p.controversy       if p.controversy       else 1
                p.sportsmanship     = player['sportsmanship']       if 'sportsmanship'      in player else p.sportsmanship     if p.sportsmanship     else 1
                p.dirtiness         = player['dirtiness']           if 'dirtiness'          in player else p.dirtiness         if p.dirtiness         else 1
                p.importantMatches  = player['importantMatches']    if 'importantMatches'   in player else p.importantMatches  if p.importantMatches  else 1
                p.loyalty           = player['loyalty']             if 'loyalty'            in player else p.loyalty           if p.loyalty           else 1
                p.pressure          = player['pressure']            if 'pressure'           in player else p.pressure          if p.pressure          else 1
                p.professionalism   = player['professionalism']     if 'professionalism'    in player else p.professionalism   if p.professionalism   else 1
                p.injuryProneness   = player['injuryProneness']     if 'injuryProneness'    in player else p.injuryProneness   if p.injuryProneness   else 1
                p.temperament       = player['temperament']         if 'temperament'        in player else p.temperament       if p.temperament       else 1
                p.versatility       = player['versatility']         if 'versatility'        in player else p.versatility       if p.versatility       else 1
                p.aggression        = player['aggression']          if 'aggression'         in player else p.aggression        if p.aggression        else 1
                p.anticipation      = player['anticipation']        if 'anticipation'       in player else p.anticipation      if p.anticipation      else 1
                p.bravery           = player['bravery']             if 'bravery'            in player else p.bravery           if p.bravery           else 1
                p.composure         = player['composure']           if 'composure'          in player else p.composure         if p.composure         else 1
                p.concentration     = player['concentration']       if 'concentration'      in player else p.concentration     if p.concentration     else 1
                p.decisions         = player['decisions']           if 'decisions'          in player else p.decisions         if p.decisions         else 1
                p.determination     = player['determination']       if 'determination'      in player else p.determination     if p.determination     else 1
                p.flair             = player['flair']               if 'flair'              in player else p.flair             if p.flair             else 1
                p.leadership        = player['leadership']          if 'leadership'         in player else p.leadership        if p.leadership        else 1
                p.offBall           = player['offBall']             if 'offBall'            in player else p.offBall           if p.offBall           else 1
                p.positioning       = player['positioning']         if 'positioning'        in player else p.positioning       if p.positioning       else 1
                p.teamwork          = player['teamwork']            if 'teamwork'           in player else p.teamwork          if p.teamwork          else 1
                p.vision            = player['vision']              if 'vision'             in player else p.vision            if p.vision            else 1
                p.workRate          = player['workRate']            if 'workRate'           in player else p.workRate          if p.workRate          else 1
                p.acceleration      = player['agility']             if 'acceleration'       in player else p.acceleration      if p.acceleration      else 1
                p.agility           = player['agility']             if 'agility'            in player else p.agility           if p.agility           else 1
                p.balance           = player['balance']             if 'balance'            in player else p.balance           if p.balance           else 1
                p.jumpingReach      = player['jumpingReach']        if 'jumpingReach'       in player else p.jumpingReach      if p.jumpingReach      else 1
                p.naturalFitness    = player['naturalFitness']      if 'naturalFitness'     in player else p.naturalFitness    if p.naturalFitness    else 1
                p.pace              = player['pace']                if 'pace'               in player else p.pace              if p.pace              else 1
                p.stamina           = player['stamina']             if 'stamina'            in player else p.stamina           if p.stamina           else 1
                p.strength          = player['strength']            if 'strength'           in player else p.strength          if p.strength          else 1

                p.save()

                if p.id:
                    updated     += 0 if new else 1
                    newRecords  += 1 if new else 0
                    if p.position == 'GR':
                        gk = Goalkeeper.objects.filter(player=p).first()

                        if not gk:
                            gk = Goalkeeper()
                            gk.player = p

                        gk.aerialAbility    = player['aerialAbility']   if 'aerialAbility'  in player else gk.aerialAbility if gk.aerialAbility else 1
                        gk.commandArea      = player['commandArea']     if 'commandArea'    in player else gk.commandArea   if gk.commandArea   else 1
                        gk.communication    = player['communication']   if 'communication'  in player else gk.communication if gk.communication else 1
                        gk.eccentricity     = player['eccentricity']    if 'eccentricity'   in player else gk.eccentricity  if gk.eccentricity  else 1
                        gk.handling         = player['handling']        if 'handling'       in player else gk.handling      if gk.handling      else 1
                        gk.kicking          = player['kicking']         if 'kicking'        in player else gk.kicking       if gk.kicking       else 1
                        gk.oneOnOne         = player['oneOnOne']        if 'oneOnOne'       in player else gk.oneOnOne      if gk.oneOnOne      else 1
                        gk.reflexes         = player['reflexes']        if 'reflexes'       in player else gk.reflexes      if gk.reflexes      else 1
                        gk.rushingOut       = player['rushingOut']      if 'rushingOut'     in player else gk.rushingOut    if gk.rushingOut    else 1
                        gk.throwing         = player['throwing']        if 'throwing'       in player else gk.throwing      if gk.throwing      else 1
                        gk.tendencyPunch    = player['tendencyPunch']   if 'tendencyPunch'  in player else gk.tendencyPunch if gk.tendencyPunch else 1
                        gk.rushingOut       = player['rushingOut']      if 'rushingOut'     in player else gk.rushingOut    if gk.rushingOut    else 1
                        gk.throwing         = player['throwing']        if 'throwing'       in player else gk.throwing      if gk.throwing      else 1
                        gk.tendencyPunch    = player['tendencyPunch']   if 'tendencyPunch'  in player else gk.tendencyPunch if gk.tendencyPunch else 1
                        gk.passing          = player['passing']         if 'passing'        in player else gk.passing       if gk.passing       else 1
                        gk.firstTouch       = player['firstTouch']      if 'firstTouch'     in player else gk.firstTouch    if gk.firstTouch    else 1
                        gk.freekick         = player['freekick']        if 'freekick'       in player else gk.freekick      if gk.freekick      else 1
                        gk.penaltyTaking    = player['penaltyTaking']   if 'penaltyTaking'  in player else gk.penaltyTaking if gk.penaltyTaking else 1
                        gk.technique        = player['technique']       if 'technique'      in player else gk.technique     if gk.technique     else 1

                        gk.save()
                    else:
                        tech = Technical.objects.filter(player=p).first()

                        if not tech:
                            tech = Technical()
                            tech.player = p

                        tech.corners        = player['corners']         if 'corners'        in player else tech.corners       if tech.corners       else 1
                        tech.crossing       = player['crossing']        if 'crossing'       in player else tech.crossing      if tech.crossing      else 1
                        tech.dribbling      = player['dribbling']       if 'dribbling'      in player else tech.dribbling     if tech.dribbling     else 1
                        tech.finishing      = player['finishing']       if 'finishing'      in player else tech.finishing     if tech.finishing     else 1
                        tech.freekick       = player['freekick']        if 'freekick'       in player else tech.freekick      if tech.freekick      else 1
                        tech.heading        = player['heading']         if 'heading'        in player else tech.heading       if tech.heading       else 1
                        tech.longShots      = player['longShots']       if 'longShots'      in player else tech.longShots     if tech.longShots     else 1
                        tech.longThrows     = player['longThrows']      if 'longThrows'     in player else tech.longThrows    if tech.longThrows    else 1
                        tech.marking        = player['marking']         if 'marking'        in player else tech.marking       if tech.marking       else 1
                        tech.passing        = player['passing']         if 'passing'        in player else tech.passing       if tech.passing       else 1
                        tech.tackling       = player['tackling']        if 'tackling'       in player else tech.tackling      if tech.tackling      else 1
                        tech.technique      = player['technique']       if 'technique'      in player else tech.technique     if tech.technique     else 1
                        tech.penaltyTaking  = player['penaltyTaking']   if 'penaltyTaking'  in player else tech.penaltyTaking if tech.penaltyTaking else 1

                        tech.save()
                else:
                    errors.append(uniqueID)
        except Exception as e:
            errors.append(str(e))

    return dict(
        updated=updated,
        newRecords=newRecords,
        errors=errors
    )

def convertPlayer(player):
    p = dict(
        id                  = player.id,
        bal                 = player.bal.name,
        uniqueID            = player.uniqueID,
        name                = player.name,
        nickname            = player.nickname,
        birthDate           = f"{player.birthDate:%d/%m/%Y}",
        age                 = player.age,
        nationality         = player.nationality,
        secondNationality   = player.secondNationality,
        height              = player.height,
        weight              = player.weight,
        wage                = locale.currency(player.wage, grouping=True).replace('$', '€').replace('.00', ' p/a').replace(',', '.'),
        contractEnd         = f"{player.contractEnd:%d/%m/%Y}",
        club                = str(player.club),
        pressDescription    = player.pressDescription,
        personality         = player.personality,
        rightFoot           = player.rightFoot,
        leftFoot            = player.leftFoot,
        position            = player.position,
        currentAbility      = player.currentAbility,
        potentialAbility    = player.potentialAbility,
        hidden = dict(
            adaptability        = player.adaptability,
            ambition            = player.ambition,
            consistency         = player.consistency,
            controversy         = player.controversy,
            sportsmanship       = player.sportsmanship,
            dirtiness           = player.dirtiness,
            importantMatches    = player.importantMatches,
            loyalty             = player.loyalty,
            pressure            = player.pressure,
            professionalism     = player.professionalism,
            injuryProneness     = player.injuryProneness,
            temperament         = player.temperament,
            versatility         = player.versatility,
        ),
        mentals = dict(
            aggression      = player.aggression,
            anticipation    = player.anticipation,
            bravery         = player.bravery,
            composure       = player.composure,
            concentration   = player.concentration,
            decisions       = player.decisions,
            determination   = player.determination,
            flair           = player.flair,
            leadership      = player.leadership,
            offBall         = player.offBall,
            positioning     = player.positioning,
            teamwork        = player.teamwork,
            vision          = player.vision,
            workRate        = player.workRate,
        ),
        physicals = dict(
            acceleration    = player.agility,
            agility         = player.agility,
            balance         = player.balance,
            jumpingReach    = player.jumpingReach,
            naturalFitness  = player.naturalFitness,
            pace            = player.pace,
            stamina         = player.stamina,
            strength        = player.strength,
        ),
    )

    return p

def getExtras(p):
    technical = Technical.objects.filter(player=p['id']).first()

    if technical:
        extra = dict(
            corners         = technical.corners,
            crossing        = technical.crossing,
            dribbling       = technical.dribbling,
            finishing       = technical.finishing,
            firstTouch      = technical.firstTouch,
            freekick        = technical.freekick,
            heading         = technical.heading,
            longShots       = technical.longShots,
            longThrows      = technical.longThrows,
            marking         = technical.marking,
            passing         = technical.passing,
            penaltyTaking   = technical.penaltyTaking,
            tackling        = technical.tackling,
            technique       = technical.technique,
        )
    else:
        goalkeeper = Goalkeeper.objects.filter(player=p['id']).first()
        if goalkeeper:
            extra = dict(
                aerialAbility   = goalkeeper.aerialAbility,
                commandArea     = goalkeeper.commandArea, 
                communication   = goalkeeper.communication, 
                eccentricity    = goalkeeper.eccentricity, 
                handling        = goalkeeper.handling, 
                kicking         = goalkeeper.kicking,
                oneOnOne        = goalkeeper.oneOnOne,
                reflexes        = goalkeeper.reflexes,
                rushingOut      = goalkeeper.rushingOut,
                tendencyPunch   = goalkeeper.tendencyPunch,
                throwing        = goalkeeper.throwing,
                passing         = goalkeeper.passing,
                firstTouch      = goalkeeper.firstTouch,
                freekick        = goalkeeper.freekick,
                penaltyTaking   = goalkeeper.penaltyTaking,
                technique       = goalkeeper.technique,
            )
    
    p.update({'extras': extra})
    return p

def convertCSVtoPlayer(csv_reader, cont):
    players = []

    for csv in csv_reader:
        if cont == 0:
            cont += 1
        else:
            try:
                player = dict(
                    uniqueID            = csv[2],
                    name                = csv[3],
                    birthDate           = datetime.strptime(csv[4].split(' ')[0], '%d/%m/%Y'),
                    age                 = int(csv[5]),
                    nationality         = csv[6],
                    secondNationality   = csv[7],
                    height              = int(csv[8].split(' ')[0]),
                    weight              = int(csv[9].split(' ')[0]),
                    wage                = csv[10].replace('€', '').replace(',', '').split(' ')[0].replace('\x80', ''),
                    contractEnd         = datetime.strptime(csv[11], '%d/%m/%Y'),
                    club                = csv[12],
                    pressDescription    = csv[13],
                    personality         = csv[14],
                    rightFoot           = csv[16],
                    leftFoot            = csv[79],
                    position            = csv[15],
                    currentAbility      = csv[17],
                    potentialAbility    = csv[18],
                    adaptability        = csv[19],
                    ambition            = csv[20],
                    consistency         = csv[21],
                    controversy         = csv[22],
                    sportsmanship       = csv[23],
                    dirtiness           = csv[24],
                    importantMatches    = csv[25],
                    loyalty             = csv[26],
                    pressure            = csv[27],
                    professionalism     = csv[28],
                    injuryProneness     = csv[29],
                    temperament         = csv[30],
                    versatility         = csv[31],
                    aggression          = csv[78],
                    anticipation        = csv[65],
                    bravery             = csv[66],
                    composure           = csv[67],
                    concentration       = csv[76],
                    decisions           = csv[77],
                    determination       = csv[68],
                    flair               = csv[75],
                    leadership          = csv[69],
                    offBall             = csv[72],
                    positioning         = csv[73],
                    teamwork            = csv[71],
                    vision              = csv[70],
                    workRate            = csv[74],
                    acceleration        = csv[32],
                    agility             = csv[33],
                    balance             = csv[35],
                    jumpingReach        = csv[37],
                    naturalFitness      = csv[34],
                    pace                = csv[39],
                    stamina             = csv[38],
                    strength            = csv[36],
                    corners             = csv[40],   
                    crossing            = csv[41],   
                    dribbling           = csv[42],       
                    finishing           = csv[43],       
                    firstTouch          = csv[44],        
                    freekick            = csv[45],   
                    heading             = csv[46],   
                    longShots           = csv[47],       
                    longThrows          = csv[48],       
                    marking             = csv[49],   
                    passing             = csv[50],   
                    tackling            = csv[52],   
                    penaltyTaking       = csv[51],           
                    technique           = csv[53],
                    aerialAbility       = csv[56],
                    commandArea         = csv[57],
                    communication       = csv[58], 
                    eccentricity        = csv[59], 
                    handling            = csv[60], 
                    throwing            = csv[61],
                    kicking             = csv[62],
                    oneOnOne            = csv[64],
                    reflexes            = csv[63],
                    rushingOut          = csv[54],
                    tendencyPunch       = csv[55],
                )
                players.append(player)
            except Exception as e:
                pass
    
    return players
class PlayersCSV(APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request):
        uploaded = []
        sent = []
        st = status.HTTP_500_INTERNAL_SERVER_ERROR

        balID = self.request.GET.get('bal', None)
        if balID:
            bal = Bal.objects.filter(id=balID).first()
            if not bal:
                bal = Bal.objects.first()
        else:
            bal = Bal.objects.first()
        
        myfile = request.FILES['players']     
        fs = FileSystemStorage()
        filename = fs.save('sheets/{}'.format(myfile.name), myfile)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url

        try:
            with open('.'+excel_file, encoding="ISO-8859-1") as file:
                csv_reader = csv.reader(file, delimiter=';')
                players = convertCSVtoPlayer(csv_reader, 0)
                sent = len(players)
                uploaded = convertData(players, bal)
                st = status.HTTP_201_CREATED
                if sent > uploaded['updated'] + uploaded['newRecords']:
                    st = status.HTTP_206_PARTIAL_CONTENT
        except Exception as e:
            response = {
                'error': str(e)
            }
            fs.delete(filename)
            return Response(response, st)

        fs.delete(filename)

        response = {
            'sent': sent,
            'uploaded': uploaded,
        }

        return Response(response, st)

class PlayersAPI(APIView):
    # permission_classes = (IsAuthenticated, )

    def delete(self, request, uid):
        response = []
        st = status.HTTP_500_INTERNAL_SERVER_ERROR

        player = Player.objects.filter(uniqueID=uid).first()

        if player:
            player.delete()
            st = status.HTTP_200_OK
        else:
            st = status.HTTP_404_NOT_FOUND
            
        return Response(response, status=st)

    def get(self, request, uid=None):
        response = []
        st = status.HTTP_500_INTERNAL_SERVER_ERROR

        club = self.request.GET.get('club', None)
        nationality = self.request.GET.get('nationality', None)
        name = self.request.GET.get('name', None)

        players = Player.objects
        if uid != None:
            players = players.filter(uniqueID=uid)
        if club != None:
            players = players.filter(club__name__icontains=club)
        if nationality != None:
            players = players.filter(nationality=nationality)
        if name != None:
            players = players.filter(name__icontains=name)
        players = players.all()

        if players is not None and len(players) > 0:
            for player in players:
                p = convertPlayer(player)
                p = getExtras(p)
                response.append(p)
            st = status.HTTP_200_OK
        else:
            st = status.HTTP_400_BAD_REQUEST
            
        return Response(response, status=st)

    def post(self, request):
        st = status.HTTP_500_INTERNAL_SERVER_ERROR
        sent = 0
        uploaded = dict()

        data = get_request_data(request)

        if len(data) > 0:
            try:
                sent = len(data)
                st = status.HTTP_201_CREATED
                balID = self.request.GET.get('bal', None)
                if balID:
                    bal = Bal.objects.filter(id=balID).first()
                    if not bal:
                        bal = Bal.objects.first()
                else:
                    bal = Bal.objects.first()
                uploaded = convertData(data, bal)
                if sent > uploaded['updated'] + uploaded['newRecords']:
                    st = status.HTTP_206_PARTIAL_CONTENT
            except:
                pass

        response = {
            'sent': sent,
            'uploaded': uploaded,
        }

        return Response(response, st)

class PerksAPI(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        response = []
        st = status.HTTP_500_INTERNAL_SERVER_ERROR
            
        return Response(response, status=st)
