from django import forms

class BeatUploadForm(forms.Form):
    is_submitted = forms.BooleanField(widget=forms.HiddenInput(), initial=False, required=False)
    file = forms.FileField(
        label='Upload Beat',
        help_text='Max. 42 megabytes',
        widget=forms.FileInput(attrs={'accept': 'audio/mpeg'})
    )