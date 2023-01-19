from django import forms
from django.forms import ModelForm
from .models import Employee


class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre", required=False)
    url = forms.URLField(label="Tu sitio web", required=False)
    comment = forms.CharField(label="Tu comentario", required=False)


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre:",
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'class': 'probando'})
    )
    email = forms.EmailField(label="Email:", max_length=50, required=False)
    message = forms.CharField(label="Mensaje")

    def clean_name(self):
        name = self.cleaned_data["name"]
        if name != 'Open':
            raise forms.ValidationError(
                "Tan solo el valor Open está permitido para este campo"
            )
        else:
            return name


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        # fields = ['name', 'last_name', 'email']
        fields = '__all__'
        # exclude = ['email']
        extra_fields = ['salary']
        widgets = {
            'name': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
        error_messages = {
            'name': {
                'max_length': "This writer's name is too long.",
            },
        }
