from django import forms
forms app1.
class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'