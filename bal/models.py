import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from jsonfield import JSONField

# Create your models here.

class Bal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    launch = models.DateField(auto_now_add=True)
    endDate = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name

class Club(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default=None, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uniqueID = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, default=None, null=True, blank=True)
    birthDate = models.DateField()
    age = models.PositiveIntegerField(default=15, validators=[MinValueValidator(15)])
    nationality = models.CharField(max_length=100) 
    secondNationality = models.CharField(max_length=100, default=None, null=True, blank=True)
    height = models.PositiveIntegerField(default=150, validators=[MinValueValidator(150), MaxValueValidator(212)])
    weight = models.PositiveIntegerField(default=55, validators=[MinValueValidator(55), MaxValueValidator(120)])
    wage = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    contractEnd = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True)
    pressDescription = models.CharField(max_length=40)
    personality = models.CharField(max_length=40)
    rightFoot = models.CharField(max_length=20, default='Muito Forte')
    leftFoot = models.CharField(max_length=20, default='Muito Fraco')
    position = models.CharField(max_length=30)
    currentAbility = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(200)])
    potentialAbility = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(200)])
    adaptability = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    ambition = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    consistency = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    controversy = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    sportsmanship = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dirtiness = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    importantMatches = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    loyalty = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    pressure = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    professionalism = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    injuryProneness = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    temperament = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    versatility = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    aggression = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    anticipation = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    bravery = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    composure = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    concentration = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    decisions = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    determination = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    flair = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    leadership = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    offBall = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    positioning = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    teamwork = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    vision = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    workRate = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    acceleration = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    agility = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    balance = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    jumpingReach = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    naturalFitness = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    pace = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    stamina = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    strength = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    bal = models.ForeignKey(Bal, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.nickname if self.nickname else self.name

class Technical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    corners = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    crossing = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    dribbling = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    finishing = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    firstTouch = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    freekick = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    heading = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    longShots = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    longThrows = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    marking = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    passing = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    penaltyTaking = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    tackling = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    technique = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.nickname if self.player.nickname else self.player.name

class Goalkeeper(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aerialAbility = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)]) 
    commandArea = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)]) 
    communication = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)]) 
    eccentricity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)]) 
    handling = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    kicking = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    oneOnOne = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    reflexes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    rushingOut = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    tendencyPunch = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    throwing = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    freekick = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    passing = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    firstTouch = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    penaltyTaking = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    technique = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.player.nickname if self.player.nickname else self.player.name

class Perk(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True, default=None)
    stats = JSONField()
    category = models.CharField(max_length=1, default='V')
    bal = models.ForeignKey(Bal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TrainingSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bal = models.ForeignKey(Bal, on_delete=models.CASCADE)
    initDate = models.DateField(auto_now_add=True)
    endDate = models.DateField()
    visiblePerks = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    hiddenPerks = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

class Training(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    trainingSession = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
    creation = models.DateField(auto_now_add=True)
    attributes = JSONField(default=None)

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    init = models.DateTimeField(auto_now_add=True)
    end = models.DateField(auto_now=True)
    response = JSONField(default=None)

