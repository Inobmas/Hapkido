from django.contrib import admin
from .models import Person, Trainer, Customer, Student, Attendant


admin.site.register(Person)
admin.site.register(Trainer)
admin.site.register(Customer)


class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "person",
        "attendant",
    )


admin.site.register(Student, StudentAdmin)


class AttendantAdmin(admin.ModelAdmin):
    list_display = (
        "person",
        "get_student",
        "relationship",
    )

    def get_student(self, obj):
        students = obj.student_set.all()
        return ", ".join(
            [
                student.person.name + " " + student.person.last_name
                for student in students
            ]
        )

    get_student.short_description = "Estudiante"


admin.site.register(Attendant, AttendantAdmin)
