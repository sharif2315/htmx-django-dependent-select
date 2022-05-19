from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin

from .models import Course, Module, Submodule


class UniversityForm(DynamicFormMixin, forms.Form):

    def module_choices(form):
        course = form['course'].value()
        filtered_modules = Module.objects.filter(course=course)
        return filtered_modules
    
    def submodules_choices(form):
        module = form['modules'].value()
        filtered_submodules = Submodule.objects.filter(module=module)
        return filtered_submodules

    # dont need initial select value
    # def initial_module(form):
    #     course = form['course'].value()
    #     return Module.objects.filter(course=course).first()     
    
    # course field
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        # initial=Course.objects.first()
    )

    # module field
    modules = DynamicField(
        forms.ModelChoiceField,
        queryset=module_choices,
        # initial=initial_module
    )

    submodules = DynamicField(
        forms.ModelChoiceField,
        queryset=submodules_choices
    )