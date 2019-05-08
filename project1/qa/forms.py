from django import forms
from .models import Day, Comment


class DayCreateForm(forms.ModelForm):

    class Meta:
        model = Day
        fields = '__all__'


class CommentCreateForm(forms.ModelForm):

    def __int__(self, *args, **kwargs):
        super().__int__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text', 'date')
