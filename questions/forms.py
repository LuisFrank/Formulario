from django import forms
from bootstrap_datepicker.widgets import DatePicker
from django.forms.models import inlineformset_factory
from .models import File, Statement


class FileForm(forms.ModelForm):

    SEXO_CHOICES = (
        ('M', "Masctulino "),
        ('F', "Feminino"))

    CHOICES = [(True, 'SI'),
               (False, 'NO')]
    region = forms.CharField(label='Region', max_length=100)
    province = forms.CharField(label='Provincia', max_length=100)
    district = forms.CharField(label='Distrito')
    community = forms.CharField(label='Comunidad')
    address = forms.CharField(label='Dirección')
    family_name = forms.CharField(label='Nombre de la familia')
    intervention_sector = forms.CharField(label='Sector de intervención( Según mapa del distrito)')
    reluctant_houses = forms.ChoiceField(label='Casas renuente o cerrada( solo cuando corresponda)', choices=CHOICES,
                                         widget=forms.RadioSelect(), required=False)
    members = forms.IntegerField(label='N° de integrantes')
    sex = forms.ChoiceField(label='Sexo ', choices=SEXO_CHOICES)
    registration_date = forms.DateField(label='Fecha', input_formats=['%d/%m/%Y'], widget=DatePicker(
            options={
                "format": "dd/mm/yyyy",
                "autoclose": True
            }
        ))

    class Meta:
        model = File
        fields = ('region', 'province', 'district', 'community', 'address', 'family_name', 'intervention_sector',
                  'reluctant_houses', 'members', 'registration_date', 'sex',)


class StatementForm(forms.ModelForm):
    CHOICES = (
        ('SI', "SI "),
        ('NO', "NO"))

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
    answer_value = forms.ChoiceField(label='Respuesta', choices=CHOICES)
    title = forms.CharField(label='Pregunta', max_length=200, widget=forms.Textarea)

    class Meta:
        model = Statement
        fields = ('order', 'title', 'answer_value')


StatementFormset = inlineformset_factory(File, Statement, form=StatementForm, extra=17,
                                         fields=('order', 'title',
                                                 'answer_value',), )
StatementFormsetEdit = inlineformset_factory(File, Statement, form=StatementForm, extra=0, fields=('order', 'title',
                                                                                                   'answer_value',), )
