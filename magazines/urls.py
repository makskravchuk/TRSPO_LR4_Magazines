from django.urls import path

from magazines.views import MagazineListAPIView, MagazineAPIView

urlpatterns = [path("magazines/", MagazineListAPIView.as_view()),
               path("create-magazine/", MagazineAPIView.as_view()),
               path("magazine/<int:pk>", MagazineAPIView.as_view()), ]
