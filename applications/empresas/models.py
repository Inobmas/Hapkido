from django.db import models
from .choices import DOCUMENT_OPTIONS


class Company(models.Model):
    business_name = models.CharField("Razon_Social", max_length=30, default="")
    legal_nature = models.CharField("Naturaleza_juridica", max_length=30, default="")
    nit = models.CharField("NIT", max_length=11, default="")
    legal_representative_name = models.CharField(
        "Nombre_Representante_Legal", max_length=60, default=""
    )
    doc_type_legal_representative = models.CharField(
        "Tipo_Doc_Representante_Legal",
        max_length=20,
        choices=DOCUMENT_OPTIONS,
        default="cedula_ciudadania",
    )
    legal_representative_doc_number = models.CharField(
        "Num_Doc_Representante_Legal",
        max_length=15,
        default="",
    )
    cell_phone_legal_representative = models.CharField(
        "Celular_Representante_Legal", max_length=15, default=""
    )
    legal_representative_email = models.EmailField(
        "Email_Representante_Legal", max_length=60, null=True
    )

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return f"{self.business_name}{self.legal_nature}{self.nit}"


class Club(models.Model):
    name = models.CharField("Nombre", max_length=30, default="")
    address = models.CharField("Direccion", max_length=40, default="")
    cell_phone = models.CharField("Celular", max_length=15, default="")
    email = models.EmailField("Email", max_length=60, null=True)

    class Meta:
        verbose_name = "Club"
        verbose_name_plural = "Clubes"

    def __str__(self):
        return f"{self.name}{self.address}"
