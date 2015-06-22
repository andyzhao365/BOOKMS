from django.contrib import admin
from bookapp.models import *

#class BookAdmin(admin.ModelAdmin):
    # list_display = (id','isbn', 'title', 'author','translator','publisher','type',)
    # list_filter = ('type','publisher',)
    # search_fields = (id','title','isbn',)
    # list_per_page=20

admin.site.register(Book)