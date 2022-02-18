from django.contrib import admin
from .models import News, Category
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# Register your models here.

class NewsadminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'



class NewsAdmin(admin.ModelAdmin):
    form = NewsadminForm
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ( 'title', 'category', 'content', 'photo', 'get_photo', 'created_at', 'views', 'updated_at', 'is_published', )
    readonly_fields = ('get_photo','views', 'updated_at', 'created_at', )
    save_on_top = True

    def get_photo(self,obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75" >')
        else:
            return 'фото не встановлено'



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
