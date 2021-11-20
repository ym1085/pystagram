# from django.contrib import admin

from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDelete, PhotoDetail, PhotoUpdate

app_name = "photo"
urlpatterns = [
    path("", PhotoList.as_view(), name='index'), # 아무것도 안 들어온 경우
    path("create/", PhotoCreate.as_view, name='create'),
    path("delete/<int:pk>", PhotoDelete.as_view, name='delete'),
    path("update/<int:pk>", PhotoUpdate.as_view, name='update'),
    path("detail/<int:pk>", PhotoDetail.as_view, name='detail'),
]
