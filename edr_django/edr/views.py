# from django.shortcuts import render

from django.shortcuts import redirect, render
from .models import Image
from .forms import ImageForm


def index(request):
    context = {}
    return render(request, "edr/index.html", context)

def disclaimer(request):
    context = {}
    return render(request, "edr/disclaimer_screen.html", context)

# def assess(request):
#     context = {}
#     return render(request, "edr/assess_screen.html", context)

def list(request):
    context = {}
    return render(request, "edr/list_screen.html", context)

def results(request, filename):
    context = {'image': filename}
    return render(request, "edr/results_screen.html", context)

def assess(request):
    print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'Upload as many files as you want!'
    # Handle file upload
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            newimg = Image(imgfile=request.FILES['imgfile'])
            newimg.save()

            # Redirect to the image list after POST
            return redirect('results/'+newimg.imgfile.name)
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = ImageForm()  # An empty, unbound form

    # Load images for the list page
    images = Image.objects.all()

    # Render list page with the images and the form
    context = {'images': images, 'form': form, 'message': message}
    return render(request, 'edr/assess_screen.html', context)