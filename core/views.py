from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path

from .models import Course, Module, Submodule
from .forms import UniversityForm

def courses_view(request):
    form = UniversityForm()
    context = {'form': form}
    return render(request, 'university.html', context)


def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'university.html', context)


def modules_view(request):
    form = UniversityForm(request.GET)
    return HttpResponse(form['modules'])


def modules(request):
    try:       
        course = request.GET.get('course')
        modules = Module.objects.filter(course=course)
        context = {'modules': modules}
        return render(request, 'partials/modules.html', context)

    except ValueError:
        return render(request, 'partials/modules.html')


def submodules_view(request):
    form = UniversityForm(request.GET)
    return HttpResponse(form['submodules'])


def submodules(request):
    try:
        module = request.GET.get('course')
        submodules = Submodule.objects.filter(module=module)
        context = {'submodules': submodules}
        return render(request, 'partials/submodules.html', context)

    except ValueError:
        return render(request, 'partials/submodules.html')
