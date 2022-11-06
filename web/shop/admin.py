from django.contrib import admin
from . models import Contact, Product, Orders , Poster , OrderUpdate

# Register your models here.

admin.site.register(Product)
admin.site.register(Poster)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
