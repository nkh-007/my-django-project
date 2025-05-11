from django.contrib import admin
from .models import Stud


class StudAdmin(admin.ModelAdmin):
    list_display=('stud_name','roll_number')
    search_fields=('stud_name','roll_number')
    list_filter=('stud_name','roll_number')
    


admin.site.register(Stud,StudAdmin)
