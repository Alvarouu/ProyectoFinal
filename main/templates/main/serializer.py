from django.core.serializers.json import DjangoJSONEncoder
from main.models import Producto

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Producto):
            return str(obj)
        return super().default(obj)