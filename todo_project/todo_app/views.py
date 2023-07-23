from django.shortcuts import render
from .models import  Todo
from .forms import TodoModel
from django.shortcuts import get_object_or_404,redirect
# Create your views here.
def index(request):
    task_list=Todo.objects.all()
    return render(request,'todo_app/index.html',dict(task_list=task_list))

def update_task(request,id):
    task = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        form=TodoModel(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = TodoModel(instance=task)
    print(form.initial)
    return render(request,'todo_app/update.html',{'form':form})
def delete_task(request,id):

     specafic_task=get_object_or_404(Todo,pk=id)
     specafic_task.delete()
     return redirect('index')


def add_task(request):

    if request.method == 'POST':

        form=TodoModel(request.POST)


        if form.is_valid():
            form.save()
            return redirect('index')

    form = TodoModel()

    return render(request,'todo_app/index.html',{'form':form})