from django.contrib import admin
from django import forms
from web.models import customers, products, appuser

class AppUserForm(forms.ModelForm):
    class Meta:
        model = appuser
        fields = '__all__'
        widgets = {
            'password': forms.PasswordInput(),
        }

class AppUserAdmin(admin.ModelAdmin):
    form = AppUserForm

# Register your models here.

admin.site.register(customers)
admin.site.register(products)
admin.site.register(appuser, AppUserAdmin)