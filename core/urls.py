from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.news_list, name="news_list"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("fiction/", views.prose_list, name="prose_list"),
    path("fiction/<slug:slug>/", views.ProseDetailView.as_view(), name="prose_detail"),
    path("poetry/", views.poetry_list, name="poetry_list"),
    path("poetry/<slug:slug>/", views.poetry_detail, name="poetry_detail"),
    path("writings/", views.writings_list, name="writings_list"),
    path("writings/<slug:slug>/", views.writings_detail, name="writings_detail"),
    path("interviews/", views.interview_list, name="interview_list"),
    path("interviews/<slug:slug>/", views.interview_detail, name="interview_detail"),
    path("about-us/", views.AboutUsView.as_view(), name="about_us"),
    path(
        "submission/", views.SubmissionGuidelinesView.as_view(), name="sub_guidelines"
    ),
    path("author/<str:author>/", views.author_detail, name="author_detail"),
    path("search/", views.search_all_view, name="search_all"),
]
