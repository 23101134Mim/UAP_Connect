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












# ===================== 50 COMMENT LINES =====================

# 1: This file contains Django views for academics app
# 2: Handles ClassRoutine CRUD operations
# 3: Also handles Marks view for students
# 4: render function returns HTML templates
# 5: redirect is used after successful form submission
# 6: get_object_or_404 fetches object or returns 404
# 7: ClassRoutineForm is used for creating/updating routines
# 8: MarkForm is imported but not used in current views
# 9: Student model is imported to get linked student
# 10: routine_list view fetches all class routines
# 11: select_related optimizes database query for related course
# 12: routines variable passed to template as context
# 13: routine_create view handles new routine creation
# 14: form initialized with POST data if available
# 15: form.is_valid() checks form input correctness
# 16: form.save() writes data to database
# 17: redirect('routine_list') navigates back to routines page
# 18: routine_form.html template renders the form
# 19: routine_update view handles editing existing routine
# 20: get_object_or_404 ensures routine exists before editing
# 21: form initialized with instance=routine to pre-fill data
# 22: form validation updates the object if valid
# 23: routine_delete view deletes routine on POST request
# 24: Confirmation page shown before deletion
# 25: routine_confirm_delete.html displays delete confirmation
# 26: marks_list view shows marks for logged-in student
# 27: try-except handles case where user is not a student
# 28: marks filtered only for the linked student
# 29: marks passed to template as context
# 30: student variable also passed for template use
# 31: empty list assigned if no student linked
# 32: views follow standard Django function-based view pattern
# 33: All CRUD views use consistent template naming
# 34: routine_list.html displays table of all routines
# 35: routine_form.html used for both create and update forms
# 36: routine_confirm_delete.html confirms deletion
# 37: marks_list.html displays student marks in table
# 38: No authentication decorators used in this code
# 39: Error handling limited to Student.DoesNotExist
# 40: No custom messages or flash notifications
# 41: Form handling is standard Django ModelForm
# 42: routine_update uses same form as routine_create
# 43: routine_delete only deletes on POST request
# 44: get_object_or_404 simplifies error handling
# 45: Code assumes request.user is always authenticated
# 46: routines variable is a QuerySet
# 47: marks variable is a QuerySet or empty list
# 48: Code uses select_related for query optimization
# 49: Context dictionaries are simple key-value pairs
# 50: End of 50-line comment section for academics views
