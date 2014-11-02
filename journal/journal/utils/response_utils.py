from os import stat
from django.core.exceptions import ValidationError
from django.http.response import JsonResponse
from journal import status_codes


class JournalResponse(JsonResponse):
    """
    accepts a valid response (code,message) tuple in response
    """
    def __init__(self, response, data=None, extra=None, *args, **kwargs):
        data = {'status': response[0],
                'message': response[1],
                'data': data if data else {},
                'extra': extra if extra else {}}
        super(JournalResponse, self).__init__(data=data, **kwargs)

class JournalSuccessResponse(JournalResponse):

    def __init__(self, data=None, extra=None, *args, **kwargs):
        super(JournalSuccessResponse, self).__init__(response=status_codes.SUCCESS, data=data, extra=extra, **kwargs)

class JSONResponseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super(JSONResponseMixin, self).dispatch(request, *args, **kwargs)
        except ValidationError as e:
            return JournalResponse(response=status_codes.BAD_INPUT, data=e.message_dict)