import cloudinary.uploader

def upload_image(file):
    response = cloudinary.uploader.upload(file)
    return response['url']
