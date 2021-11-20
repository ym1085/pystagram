# from django.contrib import admin

from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDelete, PhotoDetail, PhotoUpdate, PhotoLike, PhotoFavorite, \
    PhotoLikeList, PhotoFavoriteList

app_name = "photo"
urlpatterns = [
    path("", PhotoList.as_view(), name='index'),
    path("like/<int:photo_id>", PhotoLike.as_view(), name='like'),
    path("favorite/<int:photo_id>", PhotoFavorite.as_view(), name='favorite'),
    path("like/", PhotoLikeList.as_view(), name='like_list'),
    path("favorite/", PhotoFavoriteList.as_view(), name='favorite_list'),
    path("create/", PhotoCreate.as_view(), name='create'),
    path("delete/<int:pk>", PhotoDelete.as_view(), name='delete'),
    path("update/<int:pk>", PhotoUpdate.as_view(), name='update'),
    path("detail/<int:pk>", PhotoDetail.as_view(), name='detail'),
]

# 메인 화면 이미지 안 나오는 부분 패키지 추가
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
