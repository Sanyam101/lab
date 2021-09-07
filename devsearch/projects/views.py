from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse, response
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'projectObj':projectObj, 'tags':tags})

@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        print (request.POST)
        form = ProjectForm(request.POST, request.FILES)
        # django can check the validity of required fields 
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        print (request.POST)
        form = ProjectForm(request.POST, request.FILES, instance=project)
        # django can check the validity of required fields 
        if form.is_valid():
            form.save()
            return redirect('projects')
            
    context = {'form':form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        print (request.POST)
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request, "projects/delete_template.html", context)