from django import forms
from django.shortcuts import render

from tasks.models import Task

# Create your views here.

# variável global para guardar as nossas tasks
tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label='nova task')


# Form auto-gerado a partir do nosso Objeto Tarefa (Task model)
class PrivateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # Especificar os campos que aparecem para o utilizador...
        # Não queremos que apareça a opção de selecionar o "user" associado à task.
        # Isso é extraído do request (quando um utilizador está com sessão iniciada)
        fields = ['name']


def index(request):
    if request.method == 'POST':
        if 'remover' in request.POST:
            if request.POST['task'] in tasks:
                tasks.remove(request.POST['task'])
        elif 'adicionar' in request.POST:
            form = NewTaskForm(request.POST)
            if form.is_valid():
                tasks.append(form.cleaned_data['task'])

    form = NewTaskForm()
    return render(request, 'tasks/index.html', {'tasks': tasks, 'form': form})


def privada(request):
    if request.method == 'POST':
        if 'remover' in request.POST:
            Task.objects.filter(name=request.POST['task']).delete()

        elif 'adicionar' in request.POST:
            form = PrivateTaskForm(request.POST)
            if form.is_valid():
                # Transformar form em Objeto Tarefa sem guardar na base de dados
                task = form.save(commit=False)
                # Preencher o campo user a partir do request
                task.user = request.user
                # Guardar o Objeto completo na base de dados
                task.save()

    # Se recebermos um GET, devolver um form vazio.
    form = PrivateTaskForm()
    # Obter todas as tasks atualmente presentes na base de dados para o utilizador com sessão iniciada
    #   e enviá-las para o template.
    private_tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/privada.html', {'tasks': private_tasks, 'form': form})
