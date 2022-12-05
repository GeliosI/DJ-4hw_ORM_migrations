from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    studens_list = Student.objects.prefetch_related('teachers').order_by(ordering)
    template = 'school/students_list.html'
    context = {'studens_list': studens_list}

    return render(request, template, context)
