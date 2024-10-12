import random
from itertools import chain

from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView

from .models import (
    AboutUs,
    Home,
    Interview,
    News,
    Poetry,
    Prose,
    SubmissionGuidelines,
    Writings,
)


def custom_upload_file(request):
    if request.method == "POST":
        # Dosya yükleme işlemleri
        return HttpResponse("Dosya yüklendi.")
    return render(request, "upload.html")  # Yükleme sayfası


def home(request):
    home_articles = (
        Home.objects.filter(is_active=True)
        .only("title", "author", "thumbnail", "created_at")
        .order_by("-created_at")[:20]
    )
    top_5_articles = home_articles[:5]
    remaining_articles = home_articles[5:]
    context = {
        "top_5_articles": top_5_articles,
        "remaining_articles": remaining_articles,
    }
    return render(request, "home.html", context)


class NewsListView(ListView):
    model = News
    template_name = "news_list.html"
    context_object_name = "news"
    paginate_by = 16

    def get_queryset(self):
        return News.objects.filter(is_active=True)


class NewsDetailView(DetailView):
    model = News
    template_name = "news_detail.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_id = self.object.id
        context["related_news"] = (
            News.objects.filter(is_active=True)
            .exclude(id=news_id)
            .order_by("-created_at")[:5]
        )
        return context


class ProseListView(ListView):
    model = Prose
    template_name = "prose_list.html"
    context_object_name = "prose_list"
    paginate_by = 16

    def get_queryset(self):
        return Prose.objects.filter(is_active=True)


class ProseDetailView(DetailView):
    model = Prose
    template_name = "prose_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        prose_id = self.object.id
        context["related_prose"] = Prose.objects.filter(is_active=True).exclude(
            id=prose_id
        )[:5]
        return context


class PoetryListView(ListView):
    model = Poetry
    template_name = "poetry_list.html"
    context_object_name = "poetry_list"
    paginate_by = 16

    def get_queryset(self):
        return Poetry.objects.filter(is_active=True)


class PoetryDetailView(DetailView):
    model = Poetry
    template_name = "poetry_detail.html"
    context_object_name = "poetry"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poetry_id = self.object.id
        context["related_poetry"] = (
            Poetry.objects.filter(is_active=True)
            .exclude(id=poetry_id)
            .order_by("-created_at")[:5]
        )
        return context


class WritingsListView(ListView):
    model = Writings
    template_name = "writings_list.html"
    context_object_name = "writings_list"
    paginate_by = 16

    def get_queryset(self):
        return Writings.objects.filter(is_active=True)


class WritingsDetailView(DetailView):
    model = Writings
    template_name = "writings_detail.html"
    context_object_name = "writings"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        writings_id = self.object.id
        context["related_writings"] = (
            Writings.objects.filter(is_active=True)
            .exclude(id=writings_id)
            .order_by("-created_at")[:5]
        )
        return context


class InterviewListView(ListView):
    model = Interview
    template_name = "interview_list.html"
    context_object_name = "interview_list"
    paginate_by = 16

    def get_queryset(self):
        return Interview.objects.filter(is_active=True)


class InterviewDetailView(DetailView):
    model = Interview
    template_name = "interview_detail.html"
    context_object_name = "interviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interview_id = self.object.id
        context["related_interviews"] = (
            Interview.objects.filter(is_active=True)
            .exclude(id=interview_id)
            .order_by("-created_at")[:5]
        )  # İlgili mülakatları getir
        return context


def author_detail(request, author):
    queries = Q(author=author, is_active=True)

    all_writings = list(
        chain(
            Prose.objects.filter(queries)
            .values("id", "title", "content")
            .annotate(model_name=Value("prose")),
            Poetry.objects.filter(queries)
            .values("id", "title", "content")
            .annotate(model_name=Value("poetry")),
            Writings.objects.filter(queries)
            .values("id", "title", "content")
            .annotate(model_name=Value("writings")),
            Interview.objects.filter(queries)
            .values("id", "title", "content")
            .annotate(model_name=Value("interview")),
        )
    )

    context = {
        "author": author,
        "all_writings": all_writings,
    }
    return render(request, "author_detail.html", context)


def search_all_view(request):
    query = request.GET.get("q", "")
    results = []

    if query:
        search_conditions = (
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(author__icontains=query)
        )

        models = [News, Prose, Poetry, Writings, Interview]

        for model in models:
            results.extend(model.objects.filter(search_conditions, is_active=True))

    return render(
        request,
        "search_results.html",
        {"query": query, "results": results, "results_count": len(results)},
    )


class AboutUsView(DetailView):
    model = AboutUs
    template_name = "about_us.html"
    context_object_name = "about_us"

    def get_object(self):
        return AboutUs.objects.first()


class SubmissionGuidelinesView(DetailView):
    model = AboutUs
    template_name = "submission.html"
    context_object_name = "submission"

    def get_object(self):
        return SubmissionGuidelines.objects.first()


def custom_404_view(request, exception=None):

    content = render_to_string("404.html")
    return HttpResponseNotFound(content)
