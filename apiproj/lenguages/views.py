from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmer, Paradigm
from .serializers import LenguageSerializer, ParadigmSerializer, ProgrammerSerisalizer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LenguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerisalizer
