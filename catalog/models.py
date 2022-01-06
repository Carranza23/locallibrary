from django.db import models
from django.urls import reverse
# Create your models here.
class MyModelName(models.Model):
    #clase tipica para definir model, derivado de model class.

#field
    name = models.CharField(
                            max_length=20,
                            help_text="Enter field documentation."
                            )

#metadata

    class Meta:
        ordering= ['name']

    #metodos.

    def get_absolute_url(self):
        #Regressa el el acceso a URL en la instancia MyModelName.
        return reverse('model-datail-view', args=[str(self.id)])

    def __str__ (self):
        return self.name
