from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Programmer, Paradigm, Sale, SaleDetail
from .serializers import LenguageSerializer, ParadigmSerializer, ProgrammerSerisalizer, SaleSerializer, SaleDetailSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LenguageSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerisalizer


class SaleView(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetailView(viewsets.ModelViewSet):
    queryset = SaleDetail.objects.all()
    serializer_class = SaleDetailSerializer