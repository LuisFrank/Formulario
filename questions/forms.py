from django import forms
from django.forms.models import inlineformset_factory
from .models import File, Statement


class FileForm(forms.ModelForm):

    SRELEVANCE_CHOICES = (
        ('M', "Masctulino "),
        ('F', "Feminino" ))

    CHOICES = [(1, 'SI'),
               (0, 'NO')]
    region = forms.CharField(label='Region', max_length=100)
    province = forms.CharField(label='Provincia', max_length=100)
    reluctant_houses = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    address = forms.CharField(max_length=100)
    sex = forms.ChoiceField(choices=SRELEVANCE_CHOICES)

    class Meta:
        model = File
        fields = ('region', 'province', 'district', 'community', 'address', 'family_name', 'intervention_sector',
                  'reluctant_houses', 'members', 'registration_date', 'sex',)



class StatementForm(forms.ModelForm):
    CHOICES = (
        ('SI', "SI "),
        ('NO', "NO" ))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['order'].widget.attrs['style'] = "width:50"
        self.fields['order'].widget.attrs['readonly'] = True
        self.fields['title'].widget.attrs['style'] = "height:55"
        self.fields['title'].widget.attrs['readonly'] = True
        self.fields['answer_value'].widget.attrs['style'] = "width:100"
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


    order = forms.CharField(label='N°', max_length=100)
    answer_value = forms.ChoiceField(label='Respuesta' ,choices=CHOICES)
    title = forms.CharField(label='Pregunta',max_length=200, widget=forms.Textarea)
    class Meta:
        model = Statement
        fields = ('order','title', 'answer_value')




StatementFormset = inlineformset_factory(File, Statement, form=StatementForm, extra=17, fields=('order', 'title',
                                                                                               'answer_value',),)





