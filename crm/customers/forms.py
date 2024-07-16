from django import forms

from .models import Record


class RecordModelForm(forms.ModelForm):  # type: ignore
    class Meta:
        model = Record
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "city",
            "region",
            "zipcode",
        ]
