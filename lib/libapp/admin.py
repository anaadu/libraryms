from django.contrib import admin
from libapp.models import Book,IssueBooks


# Register your models here.
#admin.site.register(Book)
#admin.site.register(IssueBooks)

class BookAdmin(admin.ModelAdmin):
    list_display=['name','cat','author','price','status']
    list_filter = ['cat','status']



admin.site.register(Book,BookAdmin)
admin.site.site_header="LIBRARY DASHBOARD"
admin.site.site_title="LIBRARY ADMIN"
admin.site.index_title="library administration"


class IssuebookAdmin(admin.ModelAdmin):
    list_display=['Student_name','book_name','issued_date']

admin.site.register(IssueBooks,IssuebookAdmin)