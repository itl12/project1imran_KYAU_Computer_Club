from django import forms 
from .models import Faculty_profile


class Faculty_profile_form(forms.ModelForm):
    class Meta:
        model = Faculty_profile
        fields = '__all__'

    short_biography = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'rows': 10,  
        'cols': 180,  
        'style': 'font-size: 16px; color: green;' 
    }))
    research_interest = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'rows': 10,  
        'cols': 180,  
        'style': 'font-size: 16px; color: green;' 
    }))
    
    sorting_priority = forms.IntegerField(
        required=False,
        help_text='Integer value to sort faculty profiles sequence while showing' )