from import_export import resources
from .models import Altmetrics, RespuestasForm

class AltmetricsResource(resources.ModelResource):
    class Meta:
        model = Altmetrics
        import_id_fields = ['doi']

class RespuestasFormResource(resources.ModelResource):
    class Meta:
        model = RespuestasForm
        import_id_fields = ['mail']
        