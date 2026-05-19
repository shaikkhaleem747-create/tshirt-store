from django.contrib import admin
from .models import Tshirt,Order


class TshirtAdmin(admin.ModelAdmin):

    list_display = ['id','name','price','description']


class OrderAdmin(admin.ModelAdmin):

    list_display = ['id','customer_name','tshirt_name','size','quantity']


admin.site.register(Tshirt,TshirtAdmin)
admin.site.register(Order,OrderAdmin)