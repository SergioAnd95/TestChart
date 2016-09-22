from django import forms
from .models import Chart


class ChartFilterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region'].empty_label = None

    class Meta:
        model = Chart
        fields = ['region']
        labels = {
            'region': 'Регион'
        }
