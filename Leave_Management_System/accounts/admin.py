from django.contrib import admin
from .models import  CustomUser, Department, Role,Leaves

@admin.register(Department)
class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'dep_name',]

@admin.register(Role)
class RoleModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'role_name',]

@admin.register(CustomUser)
class CustomUserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'contact_number','department_id','role_id']

@admin.register(Leaves)
class LeavesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'department_id', 'leave_from_date','leave_to_Date', 'reason','status']

