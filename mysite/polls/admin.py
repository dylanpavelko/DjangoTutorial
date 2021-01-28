from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):		#can used super class admin.StackedInline for stacked fields
	model = Choice
	extra = 3

class QuestionAdmin(admin.ModelAdmin):
#	fields = ['pub_date','question_text']		#option to list fields all in one list in specified order
	fieldsets = [								#this option allows you to group related fields together
		(None, 					{'fields': ['question_text']}),
		('Date information', 	{'fields': ['pub_date']}),
		]
	inlines = [ChoiceInline]

	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)