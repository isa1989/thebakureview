import random
from itertools import chain

from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

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
        .only("title", "author", "image", "created_at")
        .order_by("-created_at")[:21]
    )
    top_5_articles = home_articles[:5]
    remaining_articles = home_articles[5:]
    context = {
        "top_5_articles": top_5_articles,
        "remaining_articles": remaining_articles,
    }
    return render(request, "home.html", context)


def news_list(request):
    news = News.objects.filter(is_active=True)
    context = {"news": news}
    return render(request, "news_list.html", context)


def news_detail(request, id):
    news_item = get_object_or_404(News, id=id)
    related_news = News.objects.filter(is_active=True).exclude(id=id)[:5]
    return render(
        request, "news_detail.html", {"news": news_item, "related_news": related_news}
    )


def prose_list(request):
    prose_list = Prose.objects.filter(is_active=True)
    context = {"prose_list": prose_list}
    return render(request, "prose_list.html", context)


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


def poetry_list(request):
    poetry_list = Poetry.objects.filter(is_active=True)
    context = {"poetry_list": poetry_list}
    return render(request, "poetry_list.html", context)


def poetry_detail(request, poetry_id):
    poetry_item = get_object_or_404(Poetry, id=poetry_id, is_active=True)
    related_poetry = Poetry.objects.filter(is_active=True).exclude(id=poetry_id)[:5]
    return render(
        request,
        "poetry_detail.html",
        {"poetry": poetry_item, "related_poetry": related_poetry},
    )


def writings_list(request):
    writings_list = Writings.objects.filter(is_active=True)
    context = {"writings_list": writings_list}
    return render(request, "writings_list.html", context)


def writings_detail(request, writings_id):
    writings_item = get_object_or_404(Writings, id=writings_id, is_active=True)
    related_writings = Writings.objects.filter(is_active=True).exclude(id=writings_id)[
        :5
    ]
    return render(
        request,
        "writings_detail.html",
        {"writings": writings_item, "related_writings": related_writings},
    )


def interview_list(request):
    interview_list = Interview.objects.filter(is_active=True)
    context = {"interview_list": interview_list}
    return render(request, "interview_list.html", context)


def interview_detail(request, interview_id):
    interview_item = get_object_or_404(Interview, id=interview_id, is_active=True)
    related_interviews = Interview.objects.filter(is_active=True).exclude(
        id=interview_id
    )[:5]
    return render(
        request,
        "interview_detail.html",
        {"interviews": interview_item, "related_interviews": related_interviews},
    )


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

        # Aktif olanlar için tüm modellerde arama yap
        models = [News, Prose, Poetry, Writings, Interview]

        for model in models:
            results.extend(model.objects.filter(search_conditions, is_active=True))

    return render(request, "search_results.html", {"query": query, "results": results})


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
