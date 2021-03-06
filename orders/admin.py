from os import write
from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Order, OrderItem
import csv
import datetime
from django.http import HttpResponse, response
from django.urls import reverse
from django.utils.safestring import mark_safe


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']



def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;'\
    'filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    fields = [field for field in opts.get_fields() if not field.many_to_many\
    and not field.one_to_many]
    # write first line with the field headers
    writer.writerow([field.verbose_name for field in fields])
    # write data
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'

def order_detail(obj):
    return mark_safe('<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id])))



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    def order_pdf(self):
        return mark_safe('<a href="{}">PDF</a>'.format(
            reverse('orders:admin_order_pdf', args=[self.id])))
        order_pdf.short_description = 'Invoice'

    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', order_pdf]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

    
        


