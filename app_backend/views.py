from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from app_backend.models import Enterpise

# Create your views here.
def loginView(request):

    if request.method == 'POST':        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('backend-home')
        else:
            messages.info(request, 'User/Password Incorrect')
            return redirect('login')

    context = {}
    return render(request, 'app_backend/login.html', context)

def logoutView(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def homeView(request):

    context = {}
    return render(request, 'app_backend/home.html', context) 

# -------------- Enterpise 
@login_required(login_url='login')
def enterpiseListView(request):
    """ List Enterpise  """
    queryset = Enterpise.objects.all()
    
    context = {'queryset':queryset}
    return render(request, 'app_backend/enterpise_list.html', context)

@login_required(login_url='login')
def enterpiseDetailView(request, ent_id):
    """ Show Enterpise detail  """
    query_obj = get_object_or_404(Enterpise, pk=ent_id)
    str_bus_type = str(query_obj.business_type)
    str_website = str(query_obj.website)

    context = {'query_obj':query_obj, 'str_bus_type':str_bus_type, 'str_website':str_website}
    return render(request, 'app_backend/enterpise_detail.html', context)