from django import forms
from django.core.mail.message import EmailMessage

from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome:')
    email = forms.EmailField(label='Email:', max_length=100)
    assunto = forms.CharField(max_length=100, label='Assunto:')
    mensagem = forms.CharField(label='Mensagem:', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'nome: {nome}\n e-mail: {email}\n assunto: {assunto}\n mensagem: {mensagem}'

        mail = EmailMessage(
            subject='este e um email enviado pelo sistema django2',
            body=conteudo,
            from_email='meu@dominio.com.br',
            to=['contato@seudominio.com.br'],
            headers={'Reply-To': email}
        )
        mail.send()

class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']

