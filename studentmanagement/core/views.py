from django.shortcuts import render, redirect
from .models import Student
from django.urls import reverse
from django.http import HttpResponseRedirect

from .forms import StudentForm
# Create your views here.
def index(request):
    students=Student.objects.all()
    return render(request, 'core/index.html', {
        'students':students
    })

def view_student(request, pk):
    student=Student.objects.get(pk=pk)
    return render(request, 'core/view_student.html', {
    'student':student
    })


def new(request):
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            new_student_number=form.cleaned_data['student_number']
            new_first_name=form.cleaned_data['first_name']
            new_last_name=form.cleaned_data['last_name']
            new_email=form.cleaned_data['email']
            new_field_of_study=form.cleaned_data['field_of_study']
            new_gpa=form.cleaned_data['gpa']

            new_student=Student(
                student_number=new_student_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                field_of_study=new_field_of_study,
                gpa=new_gpa
            )
            new_student.save()
            return redirect('index')
        return render(request, 'core/new.html', {
        'form':StudentForm(),
        'success':True
        })

    else:
        form=StudentForm()
        return render(request, 'core/new.html', {
            'form':StudentForm()
        })


def edit(request, id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return render(request, 'core/edit.html', {
                'form':form,
                'success':True
            })
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(instance=student)

        return render(request, 'core/edit.html', {
            'form':form
        })

def delete(request, id):
    if request.method==POST:
        student=Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
