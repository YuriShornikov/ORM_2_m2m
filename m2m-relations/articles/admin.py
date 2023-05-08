from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, ArticleTag

class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            print(form.cleaned_data)
            print(form)
            if form.cleaned_data == form:
                raise ValidationError('mistake')
        return super().clean()

class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]
    # pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass