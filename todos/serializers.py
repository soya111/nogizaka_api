from rest_framework import serializers
from .models import Member, Song, SongMembers


# class TodoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Todo
#         fields = ('id', 'title', 'body', 'flag', 'created_at', 'updated_at')


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        # fields = ('id', 'name', 'name_hiragana', 'generation', 'birthday','birthplace', )


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SongMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongMembers
        fields = "__all__"
