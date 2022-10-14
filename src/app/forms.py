from django.forms import ModelForm, TextInput, EmailInput, Textarea

from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message'
        )
        widgets = {
            'name': TextInput(
                attrs={
                    'type': 'text',
                    'name': 'name',
                    'class': 'form-control',
                    'id': 'name',
                    'placeholder': 'Your Name',
                    'required': True
                }
            ),
            'email': EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'name': 'email',
                    'id': 'email',
                    'placeholder': 'Your Email',
                    'required': True
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control',
                    'name': 'message',
                    'rows': '5',
                    'placeholder': 'Message',
                    'required': True
                }
            )
        }
