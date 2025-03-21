from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
import cloudinary.uploader
from apps.cloudinary_integration.forms import ImageUploadForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadedImage
from django.shortcuts import redirect


def upload_view(request):
    if request.method == "POST":

        form = ImageUploadForm(request.POST, request.FILES)

        if request.FILES['image'].size > 10485760:  # 10 MB in bytes
            # Handle the error, e.g., return an error message to the user
            return HttpResponse("The image file is too large. Please upload an image less than 10 MB.")

        if form.is_valid():
            # Upload image to Cloudinary
            response = cloudinary.uploader.upload(request.FILES['image'])
            image_url = response['url']

            # Create the UploadedImage instance
            UploadedImage.objects.create(
                image_url=image_url,
            )

            return render(request, "upload_template_success.html", {'url': image_url})  # Redirect to a success page or another view
        
    else:
        form = ImageUploadForm()

    return render(request, 'upload_template.html', {'form': form})
