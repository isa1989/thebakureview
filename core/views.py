from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Interview, News, Poetry, Prose, Writtings


def custom_upload_file(request):
    if request.method == "POST":
        # Dosya yükleme işlemleri
        return HttpResponse("Dosya yüklendi.")
    return render(request, "upload.html")  # Yükleme sayfası


def home(request):
    return render(request, "home.html")


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


def prose_detail(request, prose_id):
    prose_item = get_object_or_404(Prose, id=prose_id, is_active=True)
    related_prose = Prose.objects.filter(is_active=True).exclude(id=prose_id)[:5]
    return render(
        request,
        "prose_detail.html",
        {"prose": prose_item, "related_prose": related_prose},
    )


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


def writtings_list(request):
    writtings_list = Writtings.objects.filter(is_active=True)
    context = {"writtings_list": writtings_list}
    return render(request, "writtings_list.html", context)


def writtings_detail(request, writtings_id):
    writtings_item = get_object_or_404(Writtings, id=writtings_id, is_active=True)
    related_writtings = Writtings.objects.filter(is_active=True).exclude(
        id=writtings_id
    )[:5]
    return render(
        request,
        "writtings_detail.html",
        {"writtings": writtings_item, "related_writtings": related_writtings},
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
