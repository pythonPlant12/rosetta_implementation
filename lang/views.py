from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here. 
def home(request):
  trans = _('hello')
  return render(request, 'home.html', {trans: trans})