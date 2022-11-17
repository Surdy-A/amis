from django import forms
from .models import Workshop, Delegate, CalenderRegistration, Exhibition, Quiz, PrimaryCompetition

class WorkshopForm(forms.ModelForm):
    class Meta:
        model = Workshop
        fields = ['workshop_name', 'school', 'delegate']

    def __init__(self, *args, **kwargs):
        super(WorkshopForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'


class DelegateForm(forms.ModelForm):
    class Meta:
        model = Delegate
        fields = ['name', 'status_in_school', 'phone_number']

    def __init__(self, *args, **kwargs):
        super(DelegateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'

class CalenderRegForm(forms.ModelForm):
    class Meta:
        model = CalenderRegistration
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CalenderRegForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'


class PrimaryCompetitionRegForm(forms.ModelForm):
    class Meta:
        model = PrimaryCompetition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PrimaryCompetitionRegForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control my-2'
