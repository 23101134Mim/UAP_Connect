from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notice
from .forms import NoticeForm

def notice_list(request):
    notices = Notice.objects.all()
    return render(request, 'notices/notice_list.html', {'notices': notices})

def notice_create(request):
    form = NoticeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('notice_list')
    return render(request, 'notices/notice_form.html', {'form': form})

def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    form = NoticeForm(request.POST or None, request.FILES or None, instance=notice)
    if form.is_valid():
        form.save()
        return redirect('notice_list')
    return render(request, 'notices/notice_form.html', {'form': form})

def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == "POST":
        notice.delete()
        return redirect('notice_list')
    return render(request, 'notices/notice_confirm_delete.html', {'notice': notice})