from django.core.exceptions import ValidationError


class JournalFormMixin(object):

    def full_clean(self, *args, **kwargs):
        super(JournalFormMixin, self).full_clean()
        if self.errors:
            self.error_json = {error[0]: error[1][0] for error in self.errors.items()}
            raise ValidationError(self.error_json)
