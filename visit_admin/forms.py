from django.forms import ModelForm
from .models import Visit, VisitRoute

     
class VisitForm(ModelForm):
    class Meta:
        model=Visit
        fields='__all__'
      
class VisitRouteForm(ModelForm):
    class Meta:
        model=VisitRoute
        fields='__all__'
      