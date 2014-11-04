import time

from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from jsonfield.fields import JSONFormField

from accounts.constants import WRITER_STATES
from accounts.mixins import LoginRequiredMixin
from accounts.models import JournalWriter, Role
from journal import status_codes
from utils.form_utils import JournalFormMixin
from utils.response_utils import JournalResponse


class CreateWriterForm(JournalFormMixin, forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    role = JSONFormField(required=False)
    email = forms.EmailField(required=False)
    phone = forms.CharField(required=False)

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def save(self):
        d = self.cleaned_data
        journal_writer = User.objects.filter(username = d['username'])
        if journal_writer:
            raise ValidationError({'username':'Username not available'})
        journal_writer = JournalWriter()
        journal_writer.user = User.objects.create_user(d['username'], d['email'], d['password'], first_name=d['first_name'], last_name=d['last_name'])
        journal_writer.phone = d['phone']
        journal_writer.status = WRITER_STATES.NEW
        if not journal_writer.created_on:
            journal_writer.created_on = time.time()
        journal_writer.updated_on = time.time()
        journal_writer.save()

        if d['role']:
            for role_name in d['role'] :
                role = Role()
                role.name = role_name
                role.journal_writer = journal_writer
                role.save()
        self.instance = journal_writer

class CreateSessionForm(JournalFormMixin, forms.Form):

    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def clean_username(self):
        journal_writer = User.objects.filter(username = self.data['username'])
        if len(journal_writer) == 0:
            raise ValidationError('Invalid username')
        return self.data['username']

    def save(self):
        request = self.request
        d = self.cleaned_data
        user = authenticate(username=d['username'],password=d['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
        self.instance = request.session._session_key


class DeleteSessionForm(LoginRequiredMixin, JournalFormMixin, forms.Form):

    jour_session_key = forms.CharField(required=True)

    def delete(self):
        request = self.request
        login_mixin = LoginRequiredMixin()
        if not login_mixin.check_user(request=request):
            return JournalResponse(response=status_codes.INVALID_SESSION)
        logout(request)