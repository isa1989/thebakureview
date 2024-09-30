from django.contrib import admin

from .models import Interview, News, Poetry, Prose, Writtings

admin.site.register(News)
admin.site.register(Prose)
admin.site.register(Poetry)
admin.site.register(Writtings)
admin.site.register(Interview)
