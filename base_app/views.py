from django.shortcuts import render , redirect
from .form import TodoForm
from .models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    form = TodoForm()
    todos = TODO.objects.filter(user=request.user).order_by('priority')
    context = {
        "form":form,
        "todos":todos
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        form = TodoForm(request.POST, user=request.user)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')
        else:
            return render(request, 'index.html', {"form":form})


def delete_todo(request, id):
    TODO.objects.get(pk = id).delete()
    return redirect('home')