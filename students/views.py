from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def index(request):
    return render(request, 'students/index.html',{
        'students': Student.objects.all()
    })

def view_student(request, id):
        student = Student.objects.get(pk=id)
        return HttpResponseRedirect(reverse('index'))

from django.shortcuts import render
from .forms import StudentForm
from .models import Student

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = Student(
                student_number=form.cleaned_data['student_number'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                field_of_study=form.cleaned_data['field_of_study'],
                gpa=form.cleaned_data['gpa'],
            )
            new_student.save()
            return render(request, 'students/add.html', {
                'form': StudentForm(),
                'success': True
            })
        return render(request, 'students/add.html', {
            'form': form
        })
    return render(request, 'students/add.html', {
        'form': StudentForm()
    })
def edit(request, id):
    student = Student.objects.get(pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'students/edit.html', {
                'form': form,
                'success': True
            })
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {
        'form': form
    })
def delete(request,id):
    if request.method == 'POST':
      student=Student.objects.get(pk=id)
      student.delete()
    return HttpResponseRedirect(reverse('index'))


      