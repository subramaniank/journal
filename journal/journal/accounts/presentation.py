from django.forms.models import model_to_dict


def user_presentation(writer, fields=('username','email','phone')):
    writer_dict = model_to_dict(writer, fields=fields)
    user_dict = model_to_dict(writer.user,fields=['username','email','first_name','last_name'])
    writer_dict.update(user_dict)
    return writer_dict

def session_presentation(session):
    """
    Presentation for a session. Something might come in here later.
    """
    return {'username':session.request.user.username,'jour_session_key':session.instance}