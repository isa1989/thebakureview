from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/", views.NewsListView.as_view(), name="news_list"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="news_detail"),
    path("prose/", views.ProseListView.as_view(), name="prose_list"),
    path("prose/<slug:slug>/", views.ProseDetailView.as_view(), name="prose_detail"),
    path("poetry/", views.PoetryListView.as_view(), name="poetry_list"),
    path("poetry/<slug:slug>/", views.PoetryDetailView.as_view(), name="poetry_detail"),
    path("writings/", views.WritingsListView.as_view(), name="writings_list"),
    path(
        "writings/<slug:slug>/",
        views.WritingsDetailView.as_view(),
        name="writings_detail",
    ),
    path("interviews/", views.InterviewListView.as_view(), name="interview_list"),
    path(
        "interview/<slug:slug>/",
        views.InterviewDetailView.as_view(),
        name="interview_detail",
    ),
    path("about-us/", views.AboutUsView.as_view(), name="about_us"),
    path(
        "submission/", views.SubmissionGuidelinesView.as_view(), name="sub_guidelines"
    ),
    path("author/<str:author>/", views.author_detail, name="author_detail"),
    path("search/", views.search_all_view, name="search_all"),
]
