from django.db import models
from .choices import DOCUMENT_OPTIONS, GENDER_OPTIONS, GRADE_OPTIONS


class Person(models.Model):
    name = models.CharField("Nombres", max_length=30)
    last_name = models.CharField("Apellidos", max_length=30)
    identity_name = models.CharField(
        "Nombre identitario", max_length=30, blank=True, null=True
    )
    document_type = models.CharField(
        "Tipo documento",
        max_length=20,
        choices=DOCUMENT_OPTIONS,
        default="cedula_ciudadania",
    )
    document_number = models.CharField("Número Documento", max_length=15, default="")
    age = models.IntegerField("Edad")
    gender = models.CharField(
        "Género",
        max_length=10,
        choices=GENDER_OPTIONS,
        default="",
        blank=True,
        null=True,
    )
    cell_phone = models.CharField("Celular", max_length=15, default="")
    email = models.EmailField("Correo Electrónico", max_length=60, null=True)
    photo = models.ImageField("Foto", null=True)
    fingerprint = models.ImageField("Huella", null=True)
    residence_adress = models.CharField(
        "Dirección Residencia", max_length=40, default="", blank=True, null=True
    )
    ethnicity = models.CharField(
        "Etnia", max_length=20, default="", blank=True, null=True
    )
    profession = models.CharField(
        "Profesión", max_length=30, default="", blank=True, null=True
    )
    occupation = models.CharField(
        "Ocupación", max_length=30, default="", blank=True, null=True
    )
    disability = models.BooleanField("Discapacidad", default=False, blank=True)
    description_disability = models.CharField(
        "Descripción Discapacidad", max_length=500, default="", blank=True, null=True
    )
    observations = models.CharField(
        "Observaciones", max_length=500, default="", blank=True, null=True
    )

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Trainer(models.Model):
    grade = models.CharField(
        "Rango/Grado",
        max_length=20,
        choices=GRADE_OPTIONS,
        default="cinturon_blanco",
    )
    review = models.CharField("Reseña", max_length=1000, blank=True, null=True)
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, verbose_name="Datos Personales"
    )

    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"

    def __str__(self):
        return f"{self.grade} {self.person.name} {self.person.last_name}"


class Customer(models.Model):
    cipher = models.CharField("Código", max_length=30, default="")
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, verbose_name="Datos Personales"
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.cipher}{self.person.name}{self.person.last_name}"


class Attendant(models.Model):
    relationship = models.CharField("Parentesco", max_length=20, default="")
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, verbose_name="Datos Personales"
    )

    class Meta:
        verbose_name = "Acudiente"
        verbose_name_plural = "Acudientes"

    def __str__(self):
        return f"{self.person.name} {self.person.last_name}"


class Student(models.Model):
    grade = models.CharField(
        "Rango/Grado",
        max_length=20,
        choices=GRADE_OPTIONS,
        default="cinturon_blanco",
    )
    person = models.OneToOneField(
        Person, on_delete=models.CASCADE, verbose_name="Datos Personales"
    )
    attendant = models.ForeignKey(
        Attendant, on_delete=models.CASCADE, verbose_name="Acudiente"
    )

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return f"{self.person.name} {self.person.last_name}"
