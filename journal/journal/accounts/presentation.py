from django.forms.models import model_to_dict


def user_presentation(writer, fields=('username','email','phone')):
    writer_dict = model_to_dict(writer, fields=fields)
    writer_role_dict = {}
    writer_role_dict.update({'roles':[role.name for role in writer.roles.all()]})
    user_dict = model_to_dict(writer.user,fields=['username','email','first_name','last_name'])
    writer_dict.update(user_dict)
    writer_dict.update(writer_role_dict)
    return writer_dict

def session_presentation(session):
    """
    Presentation for a session. Something might come in here later.
    """
    return {'username':session.request.user.username,'jour_session_key':session.instance}