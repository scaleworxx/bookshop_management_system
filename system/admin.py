from django.contrib import admin
from .models import User, Genre, Language, Author, Book, Inventory

#---------------------------------------- Bookshop Management System : Language : Admin Class ----------------------------------------#
@admin.register(Language)
class LanguagesInline(admin.ModelAdmin): 
    pass

@admin.register(User)
class UsersInline(admin.ModelAdmin):    
    pass

#---------------------------------------- Bookshop Management System : Genre : Admin Class ----------------------------------------#
@admin.register(Genre)
class GenresInline(admin.ModelAdmin):   
    pass

#---------------------------------------- Bookshop Management System : Book : Inline Admin Class ----------------------------------#
class BooksInline(admin.TabularInline):   
    model = Book
    extra = 0

#---------------------------------------- Bookshop Management System : Author : Admin Class ----------------------------------------#
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name', 'country', 'number_of_books')
    fields = ['first_name', 'last_name', 'country', 'number_of_books']
    inlines = [BooksInline]

#---------------------------------------- Bookshop Management System : Inventory : Inline Admin Class ------------------------------#
class InventoryInline(admin.TabularInline):

    model = Inventory
    extra = 0

#---------------------------------------- Bookshop Management System : Book : Admin Class ------------------------------------------#
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('name', 'author',)
    list_filter = ('author', 'genre')
    fieldsets = (
        ('Information', {
            'fields': ('name', 'author',)
        }),
        ('About', {
            'fields': ('genre', 'language', 'synopsis',)
        }),
    )
    inlines = [InventoryInline]

#---------------------------------------- Bookshop Management System : Inventory : Admin Class ----------------------------------------#
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):

    list_display = ('book', 'status', 'id')
    list_filter = ('status','book', 'due_date')
    fieldsets = (
        ('Information', {
            'fields': ('book',  'id', 'borrower')
        }),
        ('Availability', {
            'fields': ('status', 'borrow_date', 'due_date',)
        }),
    )
