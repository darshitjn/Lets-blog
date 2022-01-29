from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blogpost

# Apply summernote to all TextField in model.
class BlogpostAdmin(SummernoteModelAdmin): 
    exclude = ('slug', )
    summernote_fields = ('content', )
    list_display = ('id','title','category','date_created', )
    list_display_links = ('id', 'title', )
    search_fields = ('title', )
    list_per_page = 25

admin.site.register(Blogpost, BlogpostAdmin)
