import datetime

from django.forms import ModelForm, DateInput, HiddenInput, TextInput, NumberInput, CheckboxInput
from django.forms import modelformset_factory
from .models import Header
from .models import Detail


class HeaderForm(ModelForm):
    class Meta:
        model = Header
        fields = ['name', 'reg_code', 'create_date', 'search_string', 'autofill_string']
        labels = {
            'name': 'Ärinimi',
            'reg_code': 'Registrikood',
            'create_date': 'Asutamis Kuupäev'

        }
        widgets = {
            'create_date': DateInput(attrs={'type': 'date', 'max': datetime.date.today()}),
            'search_string': HiddenInput(),
            'autofill_string': HiddenInput(),
        }


class DetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = ['autofill_string', 'reg_code', 'shareholder_first_name', 'shareholder_last_name',
                  'capital', 'id_code', 'founder', 'physical_person', 'shareholder_company_name',
                  'shareholder_company_reg_code']

        labels = {
            'reg_code': 'Registrikood',
            'shareholder_first_name': 'Eesnimi',
            'shareholder_last_name': 'Perekonnanimi',
            'shareholder_company_reg_code': 'Registrikood',
            'shareholder_company_name': 'Ärinimi',
            'capital': 'Osakapital',
            'id_code': 'Isikukood',
            'founder': 'Asutaja',
            'physical_person': 'Füüsiline Isik',

        }
        widgets = {
            'create_date': DateInput(attrs={'type': 'date'}),
            'autofill_string': HiddenInput(),
            'founder': CheckboxInput()
        }


detail_formset_create_physical_person = modelformset_factory(Detail,
                                                             fields=(
                                                                 'autofill_string', 'id_code', 'shareholder_first_name',
                                                                 'founder',
                                                                 'shareholder_last_name',
                                                                 'capital', 'physical_person'),
                                                             form=DetailForm, extra=5,
                                                             widgets={'autofill_string': HiddenInput(),
                                                                      'founder': HiddenInput(),
                                                                      'physical_person': HiddenInput(),
                                                                      'id_code': TextInput(
                                                                          attrs={'style': 'width: 300px',
                                                                                 'class': 'basicAutoComplete',
                                                                                 'data-url': '/id_code_autocomplete/',
                                                                                 'required': 'true'
                                                                                 }),
                                                                      'shareholder_first_name': TextInput(
                                                                          attrs={'required': 'true',
                                                                                 'style': 'width: 250px'}),
                                                                      'shareholder_last_name': TextInput(
                                                                          attrs={'required': 'true',
                                                                                 'style': 'width: 250px'}),
                                                                      'capital': NumberInput(attrs={
                                                                          'min': '1',
                                                                          'style': 'width: 150px'
                                                                      })

                                                                      })

detail_formset_update_physical_person = modelformset_factory(Detail,
                                                             fields=('id_code',
                                                                     'shareholder_first_name',
                                                                     'shareholder_last_name',
                                                                     'capital',
                                                                     'founder',
                                                                     'physical_person'),
                                                             form=DetailForm, extra=0,
                                                             widgets={'founder': HiddenInput(),
                                                                      'physical_person': HiddenInput(),
                                                                      'shareholder_first_name': TextInput(
                                                                          attrs={'readonly': 'readonly',
                                                                                 'style': 'width: 250px'}),
                                                                      'shareholder_last_name': TextInput(
                                                                          attrs={'readonly': 'readonly',
                                                                                 'style': 'width: 250px'}),
                                                                      'id_code': TextInput(
                                                                          attrs={'readonly': 'readonly',
                                                                                 'style': 'width: 300px',
                                                                                 }),
                                                                      'capital': NumberInput(attrs={
                                                                          'min': '1',
                                                                          'style': 'width: 150px'})
                                                                      })

detail_formset_create_judicial_person = modelformset_factory(Detail, fields=(
    'shareholder_company_reg_code', 'shareholder_company_name',
    'capital', 'physical_person', 'founder'),
                                                             form=DetailForm, extra=5,
                                                             widgets={'founder': HiddenInput(),
                                                                      'physical_person': HiddenInput(),
                                                                      'shareholder_company_reg_code': TextInput(
                                                                          attrs={'style': 'width: 200px',
                                                                                 'class': 'basicAutoComplete',
                                                                                 'data-url': '/reg_code_autocomplete/',
                                                                                 'required': 'true'
                                                                                 }),
                                                                      'shareholder_company_name': TextInput(
                                                                          attrs={'style': 'width: 400px',
                                                                                 'required': 'true'}
                                                                      )
                                                                      })

detail_formset_update_judicial_person = modelformset_factory(Detail, fields=(
    'shareholder_company_reg_code', 'shareholder_company_name',
    'capital', 'founder', 'physical_person'),
                                                             form=DetailForm, extra=0,
                                                             widgets={'founder': HiddenInput(),
                                                                      'physical_person': HiddenInput(),
                                                                      'shareholder_reg_code': TextInput(
                                                                          attrs={'readonly': 'readonly',
                                                                                 'style': 'width: 200px'}),
                                                                      'shareholder_company_name': TextInput(
                                                                          attrs={'readonly': 'readonly',
                                                                                 'style': 'width: 400px'}),

                                                                      })

detail_formset_view_judicial_person = modelformset_factory(Detail, fields=(
    'shareholder_company_reg_code', 'shareholder_company_name',
    'capital', 'founder'),
                                                           form=DetailForm, extra=0, widgets={
        'founder': TextInput(attrs={'readonly': 'readonly'}),
        'shareholder_company_name': TextInput(
            attrs={'readonly': 'readonly'}),
        'shareholder_reg_code': TextInput(
            attrs={'readonly': 'readonly'}),
        'capital': TextInput(
            attrs={'readonly': 'readonly'}),
    })

detail_formset_view_physical_person = modelformset_factory(Detail,
                                                           fields=(
                                                               'id_code', 'shareholder_first_name',
                                                               'shareholder_last_name',
                                                               'founder', 'capital',),
                                                           form=DetailForm, extra=0, widgets={
        'founder': TextInput(attrs={'readonly': 'readonly'}),
        'shareholder_first_name': TextInput(
            attrs={'readonly': 'readonly'}),
        'shareholder_last_name': TextInput(
            attrs={'readonly': 'readonly'}),
        'id_code': TextInput(
            attrs={'readonly': 'readonly'}),
        'capital': TextInput(
            attrs={'readonly': 'readonly'})})
