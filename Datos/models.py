from django.db import models

class Dato(models.Model):
    autor = models.TextField(blank=True,null=True,max_length=10,verbose_name='Autor')
    contenido = models.TextField(blank=False,max_length=370)
    imagen = models.ImageField(blank=True)
    update = models.DateField(auto_now_add=True,Verbose_name='Fecha alta')
    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(*args, **kwargs)
    class meta:
        db_table = 'Datos'
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        ordering = ['id']

    
