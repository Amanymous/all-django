from django.contrib import admin
from .models import Book,BookNumber,Character,Author

# admin.site.register(Book)1st

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # fields=['title','description','price','published','is_pubished','cover']
    list_display=['title','description','price','published','is_pubished','cover']
    list_filter=['is_pubished','cover']
    search_fields= ['title','description','price','published','is_pubished','cover']
admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)

# Register your models here.
