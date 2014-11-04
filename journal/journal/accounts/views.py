from django.views.generic.base import View
from accounts.forms import CreateWriterForm, CreateSessionForm, DeleteSessionForm
from accounts.presentation import user_presentation, session_presentation
from utils.response_utils import JSONResponseMixin, JournalSuccessResponse


class WriterView(JSONResponseMixin, View):

    def post(self, request):
        user_form = CreateWriterForm(request.POST)
        user_form.full_clean()
        user_form.save()
        return JournalSuccessResponse(data=user_presentation(user_form.instance))

class SessionView(JSONResponseMixin, View):

    def post(self, request, session_key=None):
        session_form = CreateSessionForm(request.POST)
        # Session form needs the request object to log in the user.
        session_form.request = request
        session_form.full_clean()
        session_form.save()
        return JournalSuccessResponse(data=session_presentation(session_form))

    def delete(self, request, session_key):
        del_session_form = DeleteSessionForm({'jour_session_key':session_key})
        # Session form needs the request object to log in the user.
        del_session_form.request = request
        del_session_form.full_clean()
        response = del_session_form.delete()
        if response:
            return response
        return JournalSuccessResponse()


