from django.shortcuts import render, redirect, get_object_or_404
from .models import ClassRoutine, Mark
from .forms import ClassRoutineForm, MarkForm
from users.models import Student

# --------------------
# ClassRoutine CRUD
# --------------------

from django.shortcuts import render, redirect, get_object_or_404
from .models import ClassRoutine
from .forms import ClassRoutineForm

# List all routines
def routine_list(request):
    routines = ClassRoutine.objects.select_related('course').all()
    return render(request, 'academics/routine_list.html', {'routines': routines})

# Create new routine
def routine_create(request):
    form = ClassRoutineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('routine_list')
    return render(request, 'academics/routine_form.html', {'form': form})

# Update routine
def routine_update(request, pk):
    routine = get_object_or_404(ClassRoutine, pk=pk)
    form = ClassRoutineForm(request.POST or None, instance=routine)
    if form.is_valid():
        form.save()
        return redirect('routine_list')
    return render(request, 'academics/routine_form.html', {'form': form})

# Delete routine
def routine_delete(request, pk):
    routine = get_object_or_404(ClassRoutine, pk=pk)
    if request.method == "POST":
        routine.delete()
        return redirect('routine_list')
    return render(request, 'academics/routine_confirm_delete.html', {'routine': routine})

# --------------------
# Marks (view only for student)
# --------------------
def marks_list(request):
    try:
        student = request.user.student
        marks = Mark.objects.filter(student=student)
    except Student.DoesNotExist:
        student = None
        marks = []  # Empty if no student linked
    return render(request, 'academics/marks_list.html', {'marks': marks, 'student': student})