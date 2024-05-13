from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Altmetrics, RespuestasForm
from .resource import AltmetricsResource, RespuestasFormResource
# Register your models here.

class AltmetricsAdmin(ImportExportModelAdmin, admin.ModelAdmin):    
    resource_class = AltmetricsResource
    list_display = ('doi', 'title', 'mendeley_readers', 'score', 'facebook', 'x', 'blogs', 'news', 'reddit', 'stackoverflow', 'policies', 'patents', 'youtube', 'wikipedia', 'year', 'total')
    list_filter = ('year',)


class RespuestasFormAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resouce_class = RespuestasFormResource
    list_display = ('mail', 'timestamp', 'genero', 'jerarquia', 'facultad', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15')
    list_filter = ('facultad',)

admin.site.register(Altmetrics, AltmetricsAdmin)
admin.site.register(RespuestasForm, RespuestasFormAdmin)

