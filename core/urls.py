from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.news_list, name="news_list"),
    path("news/<int:id>/", views.news_detail, name="news_detail"),
    path("prose/", views.prose_list, name="prose_list"),
    path("prose/<int:prose_id>/", views.prose_detail, name="prose_detail"),
    path("poetry/", views.poetry_list, name="poetry_list"),
    path("poetry/<int:poetry_id>/", views.poetry_detail, name="poetry_detail"),
    path("writtings/", views.writtings_list, name="writtings_list"),
    path(
        "writtings/<int:writtings_id>/", views.writtings_detail, name="writtings_detail"
    ),
    path("interviews/", views.interview_list, name="interview_list"),
    path(
        "interviews/<int:interview_id>/",
        views.interview_detail,
        name="interview_detail",
    ),
]
