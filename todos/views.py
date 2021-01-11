from rest_framework import generics, viewsets, status
from rest_framework.generics import GenericAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from django.urls import reverse
from .models import Member, Song, SongMembers
from .serializers import MemberSerializer, SongSerializer, SongMembersSerializer

# Create your views here.


# class ListTodo(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# class MemberViewSet(viewsets.ModelViewSet):
#     queryset = Member.objects.all()
#     serializer_class = MemberSerializer

class MemberList(GenericAPIView):

    def get(self, request):
        members = Member.objects.all()
        members = [{'id': i.id, 'name': i.name,
                    'uri': 'http://127.0.0.1:8000'+reverse('members', args=[i.id])} for i in members]
        return Response(data={'members': members}, status=status.HTTP_200_OK)


class MemberDetail(RetrieveAPIView):

    def get(self, request, pk):
        member = Member.objects.get(pk=pk)
        songs = SongMembers.objects.filter(member_id=member)
        songs = [{'id': i.song_id.id, 'name': i.song_id.name,
                  'uri': 'http://127.0.0.1:8000'+reverse('songs', args=[i.song_id.id])} for i in songs]
        return Response(data={'member': member.name, 'songs_num': len(songs), 'songs': songs}, status=status.HTTP_200_OK)


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongList(GenericAPIView):

    def get(self, request):
        songs = Song.objects.all()
        songs = [{'id': i.id, 'name': i.name,
                  'uri': 'http://127.0.0.1:8000'+reverse('songs', args=[i.id])} for i in songs]
        return Response(data={'songs': songs}, status=status.HTTP_200_OK)


class SongDetail(RetrieveAPIView):

    def get(self, request, pk):
        song = Song.objects.get(pk=pk)
        members = SongMembers.objects.filter(song_id=song)
        members = [{'id': i.member_id.id, 'name': i.member_id.name, 'uri': 'http://127.0.0.1:8000'+reverse('members', args=[i.member_id.id])}
                   for i in members]
        return Response(data={'song': song.name, 'members_num': len(members), 'members': members}, status=status.HTTP_200_OK)


class SongMembersViewSet(viewsets.ModelViewSet):
    queryset = SongMembers.objects.all()
    serializer_class = SongMembersSerializer
