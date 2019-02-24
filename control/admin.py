from django.contrib import admin
from .models import internship
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import NewUserModel
from .models import commission
# Register your models here.

admin.site.register(internship) 
admin.site.register(commission)

class NewUserModel_Inline(admin.StackedInline):
    model = NewUserModel
    can_delete = False
    verbose_name_plural = 'Kişisel Bilgiler'
 
class UserAdmin(BaseUserAdmin):
    inlines = (NewUserModel_Inline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


