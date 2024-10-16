from django.contrib import admin

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


class BaseModelAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "get_authors",
        "is_active",
        "created_at",
    )
    search_fields = ("title", "authors__name")
    filter_horizontal = ("authors",)

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    get_authors.short_description = "Müəlliflər"


class HomeModelAdmin(admin.ModelAdmin):
    list_display = ("title", "get_authors", "is_active", "created_at")
    search_fields = ("title", "authors__name")
    list_filter = ("is_active", "created_at")
    ordering = ("-created_at",)
    filter_horizontal = ("authors",)

    def get_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    get_authors.short_description = "Müəlliflər"


admin.site.register(News, BaseModelAdmin)
admin.site.register(Prose, BaseModelAdmin)
admin.site.register(Poetry, BaseModelAdmin)
admin.site.register(Writings, BaseModelAdmin)
admin.site.register(Interview, BaseModelAdmin)
admin.site.register(Author)
admin.site.register(Home, HomeModelAdmin)
admin.site.register(AboutUs)
admin.site.register(SubmissionGuidelines)
admin.site.register(AppealReaders)
