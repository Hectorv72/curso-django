from django import forms


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
