from django.contrib import admin
from .models import Position, Document, Employee, Certificate, Discipline, Exam


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'duties', 'conditions', 'requirements')

    search_fields = ('title', 'duties')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_name', 'issue_date', 'expiration_date')

    search_fields = ('department_name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'birth_date', 'phone', 'email')

    search_fields = ('full_name', 'gender', 'birth_date', 'phone', 'email')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'issue_date', 'mark')


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'hours')

    search_fields = ('title',)


class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'attempts_count', 'type')


admin.site.register(Position, PositionAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Exam, ExamAdmin)
# admin.site.register(Order, OrderAdmin)
# admin.site.register(Device, DeviceAdmin)
# admin.site.register(Customer, CustomerAdmin)
# admin.site.register(DeviceInUse, DeviceInUseAdmin)
