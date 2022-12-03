from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render

from customers.forms import ProfileForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        messages.warning(request,f'已經以{request.use.username} 登入了')
        return redirect('cafe:coffee_list')

    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user=form.save()
        messages.success(request,'註冊成功')
        return redirect('cafe:coffee_list')
        
    return render(request, 'customers/register.html',{'form':form})

@login_required
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        messages.success(request, '編輯個人檔案成功')
    return render(request, 'customers/profile.html', {'form': form})

