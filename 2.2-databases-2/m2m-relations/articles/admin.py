from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        tags = []
        main = []
        for form in self.forms:
            if self.can_delete and self._should_delete_form(form):
                continue
            if form.cleaned_data.get('is_main'):
                if not main:
                    main.append(form.cleaned_data.get('is_main'))
                else:
                    raise ValidationError('Может быть только один главный tag')
            tag = form.cleaned_data.get('tag')
            if tag in tags:
                raise ValidationError('Такой tag уже существует')
            tags.append(tag)
        if not main:
            raise ValidationError('Укажите главный tag')

        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', ]
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']