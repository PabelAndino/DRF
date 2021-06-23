from rest_framework import serializers
from .models import Language, Paradigm, Programmer


class LenguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm')


class ParadigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'name')


class ProgrammerSerisalizer(serializers.ModelSerializer):
    languages = LenguageSerializer(many=True)

    class Meta:
        model = Programmer
        fields = ('id', 'name', 'languages')

    def create(self, validated_data):
        language_data = validated_data.pop('languages')
        programmer = Programmer.objects.create(**validated_data)
        for language_data in language_data:
            Language.objects.create(programmer=programmer, **language_data)
            print(language_data)
        return programmer

    # {
    #
    #     "name": "RUBY",
    #     "paradigm": 1
    # },
    # {
    #
    #     "name": "SCALA",
    #     "paradigm": 3
    # }