import cloudinary.uploader

# Defining a function for uploading an image to Cloudinary
def upload_image(file):
    # Uploading the image using Cloudinary's uploader
    response = cloudinary.uploader.upload(file)
    
    # Returning the URL of the uploaded image
    return response['url']
