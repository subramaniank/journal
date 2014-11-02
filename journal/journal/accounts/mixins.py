from accounts.models import JournalWriter
from journal import status_codes
from utils.response_utils import JournalResponse


class LoginRequiredMixin(object):

    def check_user(self, request):
        user = request.user
        if user.is_authenticated() and user.is_active and JournalWriter.objects.get(user=user):
            return True
        elif not user.is_active:
            return False

    def dispatch(self, request, *args, **kwargs):
        if not self.check_user(request=request):
            return JournalResponse(response=status_codes.INVALID_USER)
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
