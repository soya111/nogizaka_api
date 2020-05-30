from rest_framework import generics, viewsets
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


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongMembersViewSet(viewsets.ModelViewSet):
    queryset = SongMembers.objects.all()
    serializer_class = SongMembersSerializer
