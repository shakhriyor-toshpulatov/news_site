from django.contrib import admin
from django import forms

from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    article = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_at', 'image', 'is_published']
    prepopulated_fields = {'url': ('title',)}
    list_display_links = ['id', 'title']
    search_fields = ['title', 'article']
    list_editable = ('is_published',)
    form = PostAdminForm
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    prepopulated_fields = {'url': ('name',)}
    list_display_links = ['id', 'name']


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы"""
    list_display = ("name", "email", "parent", "post", "id")
    readonly_fields = ("name", "email")
