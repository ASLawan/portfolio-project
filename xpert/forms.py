from django import forms
from .models import Service, Projects, Reviews

class ProjectsForm(forms.ModelForm):

    class Meta:
        model = Projects
        fields = '__all__'

class ServicesForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'


class ReviewsForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = '__all__'


class ServiceSearchForm(forms.Form):
    service_name = forms.CharField(label="Service Name", max_length=100, required=False)
    country = forms.CharField(label="Country", max_length=100, required=False)
    region = forms.CharField(label="Region", max_length=100, required=False)
    town = forms.CharField(label="Town", max_length=100, required=False)

    class Meta:
        fields = ['service_name', 'country', 'region', 'town']

