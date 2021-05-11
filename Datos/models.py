from django.db import models

class Dato(models.Model):
    autor = models.TextField(blank=True,null=True,max_length=10,verbose_name='Autor')
    contenido = models.TextField(blank=False,max_length=370,verbose_name='Contenido')
    imagen = models.ImageField(blank=True,verbose_name='Imagen',upload_to='Datosimg')
    update = models.DateField(auto_now_add=True,verbose_name='Fecha alta')
    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(*args, **kwargs)
    class meta:
        db_table = 'Datos'
        verbose_name = 'Dato'
        verbose_name_plural = 'Datos'
        ordering = ['id']

    
