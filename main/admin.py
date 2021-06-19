from django.contrib import admin
from .models import ShortRoutes
from .models import MediumRoutes
from .models import LongRoutes
from .models import LongRunRoutes
from .models import DestinationRoutes

admin.site.register(ShortRoutes)
admin.site.register(MediumRoutes)
admin.site.register(LongRoutes)
admin.site.register(LongRunRoutes)
admin.site.register(DestinationRoutes)
