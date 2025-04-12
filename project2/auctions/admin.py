from django.contrib import admin
from .models import Listing,bid,comment
# Register your models here.
admin.site.register(Listing)
admin.site.register(bid)
admin.site.register(comment)