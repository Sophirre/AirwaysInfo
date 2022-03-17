from django.contrib import admin
from .models import (
    Flight,
    Company,
)


admin.site.register(Flight)
admin.site.register(Company)


# Register your models here.
