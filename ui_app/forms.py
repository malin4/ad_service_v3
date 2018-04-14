from django import forms
from .models import MessagePanel


class MessagePanelForm(forms.ModelForm):
    class Meta:
        model = MessagePanel
        fields = ('advert_title', 'user', 'body')