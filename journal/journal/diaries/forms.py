import time

from django import forms

from diaries.models import Diary


class CreateDiaryForm(forms.Form):

    title = forms.CharField(required=False)
    content = forms.CharField(required=False)
    place = forms.CharField(required=False)

    def save(self, commit=False):
        """
        Does not commit the diary to the file.
        Only binds it to the form so a user can own it and save it.
        """
        d = self.cleaned_data
        diary = Diary()
        diary.title = d['title']
        diary.content = d['content']
        diary.place = d['place']

        if not diary.created_on:
            diary.created_on = time.time()
        diary.updated_on = time.time()
        self.instance = diary