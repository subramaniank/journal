from django.forms.models import model_to_dict


def diary_presentation(diary):
    diary_dict = model_to_dict(diary, exclude=['extra_params'])
    return diary_dict
