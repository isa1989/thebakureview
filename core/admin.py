from django.contrib import admin

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

admin.site.register(News)
admin.site.register(Prose)
admin.site.register(Poetry)
admin.site.register(Writings)
admin.site.register(Interview)
admin.site.register(Home)
admin.site.register(AboutUs)
admin.site.register(SubmissionGuidelines)
