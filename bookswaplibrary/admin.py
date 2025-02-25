from django.contrib import admin

# Register your models here.

from .models import Address, Author, Book, BookInstance, Genre, Member, Publisher, BookImage


admin.site.register(Address)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Member)
admin.site.register(Publisher)
admin.site.register(BookImage)