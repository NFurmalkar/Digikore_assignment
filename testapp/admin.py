from django.contrib import admin
from testapp.models import Register

# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['id','email','contact','age','address','academicLevel', 'university', 'fieldStudy', 'studyDestination', 'enrollment', 'languageProficiency']

admin.site.register(Register,RegisterAdmin)
