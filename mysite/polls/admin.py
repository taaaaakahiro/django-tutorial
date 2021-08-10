# Register your models here.
from django.contrib import admin

from .models import Choice, Question

# 管理者フォームの表示位置を変更
# class QuestionAdmin(admin.ModelAdmin):
#   fields = ['pub_date','question_text']

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3
# 管理者フォームのフィールドを区切る
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    ('text', {'fields': ['question_text']}),
    ('Date information', {'fields': ['pub_date']}),
  ]
  # 複数データを一括で挿入
  inlines = [ChoiceInline]
  # 列表示
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  # キーワード検索
  search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
