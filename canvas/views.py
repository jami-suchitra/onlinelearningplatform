from django.shortcuts import render,redirect
from .form import CanvasForm

def Canvas_create(request):
    if request.method == 'POST':
        form = CanvasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Canvas')  
        form = CanvasForm()
    return render(request, 'Canvas_form.html', {'form': form})
# Create your views here.