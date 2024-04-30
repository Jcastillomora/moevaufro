from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Altmetrics
from .resource import AltmetricsResource
# Register your models here.

class AltmetricsAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    resource_class = AltmetricsResource
    list_display = ('doi', 'title', 'mendeley_readers', 'score', 'facebook', 'x', 'blogs', 'news', 'reddit', 'stackoverflow', 'policies', 'patents', 'youtube', 'wikipedia', 'year', 'total')
    list_filter = ('year',)

admin.site.register(Altmetrics, AltmetricsAdmin)

