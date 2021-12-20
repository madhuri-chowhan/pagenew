from django import forms
# from django.forms.fields import EmailField
from django.core import validators
from django.core.exceptions import ValidationError
 
#customize validator:
# def check(value):
#     if value[0] != 'k':
#         raise ValidationError("start the name with 'k'".upper())

class formed(forms.Form):
    name = forms.CharField(max_length=50)  # validators = [check])
    email = forms.EmailField()
    # vmail = forms.EmailField(label="enter mail_id again")
    comment = forms.CharField(widget=forms.Textarea)

    # def _clean_from(self):
    #    data =  super( ).clean( )
    #    email = data['email']

    #    vmail = data['vmail']

    #    if email != vmail:
    #        raise ValidationError("incorrect mail")

    # botcatcher = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)]) 




    # def clean_botcatcher(self):
    #     botcatcher =self.cleaned_data['botcatcher']

    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("IT'S A BOT!!😠😤 ")
    #     return botcatcher