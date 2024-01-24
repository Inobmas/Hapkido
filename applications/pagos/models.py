from django.db import models

class ProductService(models.Model):

    name = models.CharField('Nombre', max_length=40, default='')
    price = models.DecimalField('Precio', max_digits=8, decimal_places=2, default=0.0)
    year = models.DateTimeField('Año')
    description = models.CharField('Descripcion', max_length=1000, default='')

    class Meta:
        verbose_name = "Producto_Servicio"
        verbose_name_plural = "Productos_Servicios"

    def __str__(self):
        return f"{self.name}{self.price}"

class Pay(models.Model):

    receipt_number = models.IntegerField('Numero_recibo')
    pay_day = models.DateTimeField('Fecha_Pago', default='')
    value_paid = models.DecimalField('Valor_Pagado', max_digits=8, decimal_places=2, default=0.0)
    payment_method = models.CharField('Metodo_Pago', max_length=20, default='')

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return f"{self.receipt_number}{self.pay_day}"
    
    


