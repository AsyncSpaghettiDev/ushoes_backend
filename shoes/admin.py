from django.contrib import admin

# Register your models here.

from .models import Brand, ShoeType, ShoeGender, ShoeColor, Shoe

admin.site.register(Brand)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(ShoeGender)
admin.site.register(Shoe)
