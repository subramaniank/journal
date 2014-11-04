from django.views.generic.base import View
from diaries.presentation import diary_presentation
from journal import status_codes
from accounts.mixins import LoginRequiredMixin
from accounts.models import JournalWriter
from diaries.forms import CreateDiaryForm
from utils.response_utils import JSONResponseMixin, JournalSuccessResponse, JournalResponse


class DiaryView(JSONResponseMixin, LoginRequiredMixin, View):

    def get(self, request, diary_id):
        writer = JournalWriter.objects.get(user=request.user)
        diary = writer.diaries.filter(id=diary_id)
        if not diary:
            return JournalResponse(response=status_codes.NOT_FOUND, data={'id':diary_id})
        return JournalSuccessResponse(data=diary_presentation(diary[0]))
        

    def post(self, request, diary_id=None):
        diary_form = CreateDiaryForm(request.POST)
        diary_form.full_clean()
        diary_form.save()
        diary = diary_form.instance
        diary.writer = JournalWriter.objects.get(user=request.user)
        diary.save()
        return JournalSuccessResponse(data={'id':diary.id})

class DiariesView(JSONResponseMixin, LoginRequiredMixin, View):

    def get(self, request):
        writer = JournalWriter.objects.get(user=request.user)
        diary_ids = writer.diaries.all().values('id')
        return JournalSuccessResponse(data=[diary['id'] for diary in diary_ids])