from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from cafe.models import Coffee
from redeem.models import Redeem

# Create your views here.
@login_required
def coffee_list(request):
    coffee = Coffee.objects.all()
    return render(request, 'cafe/coffee_list.html', {'cafe': coffee})

