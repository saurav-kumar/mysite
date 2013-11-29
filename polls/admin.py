from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.\

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text'] #if only to display without fieldsets
    '''Adding fieldsets to categorize the fields''' 
    fieldsets = [
        ('Question' , {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    '''Replace with this if want to show/hide fields
    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    '''

admin.site.register(Question, QuestionAdmin)

