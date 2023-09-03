from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from core.models import *

# Create your views here.

    
class home(TemplateView):
    template_name = "ytrasbook.html"
    def get(self, request):
        return render(request, self.template_name, None)
    