import random
from itertools import chain

from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import (
    AboutUs,
    AppealReaders,
    Author,
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
        .only("title", "authors", "thumbnail", "created_at")
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
        )
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"
    context_object_name = "author"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object

        queries = Q(authors=author, is_active=True)

        all_writings = list(
            chain(
                Prose.objects.filter(queries)
                .values("slug", "title", "content")
                .annotate(model_name=Value("prose")),
                Poetry.objects.filter(queries)
                .values("slug", "title", "content")
                .annotate(model_name=Value("poetry")),
                Writings.objects.filter(queries)
                .values("slug", "title", "content")
                .annotate(model_name=Value("writings")),
                Interview.objects.filter(queries)
                .values("slug", "title", "content")
                .annotate(model_name=Value("interview")),
                News.objects.filter(queries)
                .values("slug", "title", "content")
                .annotate(model_name=Value("news")),
            )
        )

        paginator = Paginator(all_writings, self.paginate_by)
        page_number = self.request.GET.get("page", 1)
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context["all_writings"] = page_obj
        context["results_count"] = paginator.count
        return context


class SearchView(ListView):
    template_name = "search_results.html"
    context_object_name = "results"
    paginate_by = 20

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        if not query:
            return []

        search_conditions = (
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(authors__name__icontains=query)
        )

        models = [News, Prose, Poetry, Writings, Interview]
        results = []

        for model in models:
            model_results = model.objects.filter(
                search_conditions, is_active=True
            ).distinct()
            results.extend(model_results)

        return results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")

        results_list = self.get_queryset()
        paginator = Paginator(results_list, self.paginate_by)

        page_number = self.request.GET.get("page", 1)
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context["results"] = page_obj
        context["results_count"] = paginator.count
        return context


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


class AppealReadersView(DetailView):
    model = AboutUs
    template_name = "appeal.html"
    context_object_name = "appeal"

    def get_object(self):
        return AppealReaders.objects.first()


def custom_404_view(request, exception=None):

    content = render_to_string("404.html")
    return HttpResponseNotFound(content)
