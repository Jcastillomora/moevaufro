from import_export import resources
from .models import Altmetrics

class AltmetricsResource(resources.ModelResource):
    class Meta:
        model = Altmetrics
        import_id_fields = ['doi']
        