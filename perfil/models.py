from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls  import reverse


# Create your models here.
class Perfil(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido =models.CharField(max_length=50)
    dni =models.CharField(max_length=10)
    edad =models.IntegerField()
    fecha_nacimiento=models.DateField()
    celular =models.CharField(max_length=15)
    correo =models.CharField(max_length=50)
    ciudad =models.CharField(max_length=50)
    foto=models.ImageField(upload_to="perfil",blank=True,null=True)

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.nombre

    def get_absolute_url(self):
        return reverse("proyecto-ver", kwargs={"pk": self.pk})

    def save(self):
        super().save()
        if self.foto:
            foto = Image.open(self.foto.path)
            if foto.height > 300 or foto.width > 300:
                output_size = (300, 300)
                foto.thumbnail(output_size)
                foto.save(self.foto.path)


class Descripcion(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    acerca_de =models.TextField()
    nivel_desarrollador =models.CharField(max_length=20)

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.acerca_de

class RedesSociales(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github = models.CharField(max_length=50)
    linkedin =models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.github

class Habilidades(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tecnologia = models.CharField(max_length=50)

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.tecnologia
    
class Experiencia(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    empresa = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.puesto

class Formacion(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resumen = models.TextField()
    entidad = models.CharField(max_length=50)
    fecha_inicio=models.DateField()
    fecha_fin=models.DateField()

    def __str__(self):
        """Unicode representation of Proyecto."""
        return self.entidad

class Proyectos(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    explicacion = models.TextField()
    link = models.URLField()
    imagen = models.ImageField(upload_to="proyectos",blank=True,null=True, default="buscar.jpg")


    class Meta:
        """Meta definition for Poyecto."""
        #db_table = "proyectos"
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'


    def __str__(self):
        """Unicode representation of Poyecto."""
        return self.titulo
    
    def save(self):
        super().save()
        if self.imagen:
            imagen = Image.open(self.imagen.path)
            if imagen.height > 300 or imagen.width > 300:
                output_size = (300, 300)
                imagen.thumbnail(output_size)
                imagen.save(self.imagen.path)


class Contacto(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    asunto = models.CharField(max_length=50)
