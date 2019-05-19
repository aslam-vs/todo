from django import forms

from .models import ToDo,STATUS_CHOICES


class ToDoForm(forms.Form):
	title = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Title','class':'form-control'}))
	description = forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder':'Description','class':"form-control"}))
	date = forms.RegexField(regex=r'^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$',
		widget=forms.TextInput(attrs={'placeholder':'Date example : 2019-1-11 13:57:24','class':"form-control"}))
	status = forms.ChoiceField(choices = STATUS_CHOICES, initial='In Progress', widget=forms.Select(attrs={'class':'form-control'}), required=True)

	class Meta:
		fields = ("title", "description", "date","status")

	def save(self,todo=None):
		if todo:
			todo = todo
		else:
			todo = ToDo()
		todo.title = self.data['title']
		todo.description = self.data['description']
		todo.date = self.data['date']
		todo.status = self.data['status']
		todo.save()





