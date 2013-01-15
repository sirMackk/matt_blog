from django.contrib.comments.forms import CommentForm
from django import forms
from django.forms.util import ErrorDict

class CommentFormHoneyPotted(CommentForm):
    website = forms.CharField(required=False, label=('Never send a human to do a machines job'))

    def clean_website(self):
        value = self.cleaned_data['website']
        if value:
            raise forms.ValidationError(self.fields['website'].label)
        return value

    def security_errors(self):
        errors = ErrorDict()
        for f in ["honeypot", "timestamp", "security_hash", "website"]:
            if f in self.errors:
                errors[f] = self.errors[f]
        return errors

