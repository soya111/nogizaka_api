# from django.urls import path, include
from rest_framework import routers

from .views import MemberViewSet, SongViewSet, SongMembersViewSet

router = routers.DefaultRouter()
router.register(r'members', MemberViewSet, basename="members")
router.register(r'songs', SongViewSet, basename="songs")
router.register(r'songmembers', SongMembersViewSet, basename="songmembers")
# router.register(r'todos', TodoViewSet, basename="todos")


urlpatterns = router.urls
