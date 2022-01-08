from django.contrib import admin

# Register your models here.
from .models import Book, Author, Genre, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

#Define la clase de autor
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name','date_of_birth','date_of_death')
    pass

#registra admin class con el modelo asociado
admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','display_genre')
    def display_genre(self):
        """Crear un string para el genero.Esto es requerido por el admin"""
        return ',' .join(genre.name for genre in self.genre.all()[:3])
    pass

#registra admin class con el modelo asociado
admin.site.register(Book, BookAdmin)

class BookInstanceAdmin(admin.ModelAdmin):
    list_filter=('status','due_back')
    pass

#registra admin class con el modelo asociado
admin.site.register(BookInstance, BookInstanceAdmin)
