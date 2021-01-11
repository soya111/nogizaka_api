from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from .views import SongViewSet, SongMembersViewSet, MemberList, MemberDetail, SongList, SongDetail

# router = routers.DefaultRouter()
# router.register(r'members', MemberViewSet, basename="members")
# router.register(r'songs', SongViewSet, basename="songs")
# router.register(r'songmembers', SongMembersViewSet, basename="songmembers")


# urlpatterns = router.urls
urlpatterns = [
    path("jwt-token/", obtain_jwt_token),
    path("members/<int:pk>/", MemberDetail.as_view(), name="members"),
    path("members/", MemberList.as_view()),
    path("songs/<int:pk>/", SongDetail.as_view(), name="songs"),
    path("songs/", SongList.as_view()),
]
