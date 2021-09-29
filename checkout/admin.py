from django.contrib import admin
from checkout.models import Order
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    readonly_fields = ('total_cost', 'date', 'stripe_pid')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }
