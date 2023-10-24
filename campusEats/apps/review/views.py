from django.shortcuts import render, redirect
from apps.restaurants.models import Restaurant #I assume were using render but this can change.
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from datetime import datetime

def cancel_review(request, restaurant_id):
    # Do any necessary processing and retrieve the restaurant details
    # For example, you can query the database to get restaurant data
    print(restaurant)
    restaurant = Restaurant.objects.get(pk=restaurant_id)  # Adjust this according to your model
    print(restaurant_id)
    # Render the "Cancel Review" template with the restaurant context variable
    return render(request, 'cancel_review.html', {'restaurant': restaurant})

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.UserID = request.user  # Assuming we are using Django's authentication system
            new_review.save()
            return redirect('some_view_name')  # Redirect to a confirmation page or the review list page
    else:
        form = ReviewForm()

    context = {'form': form}
    return render(request, 'review/create_review.html', context)

def display_reviews(request, restaurant_id):
    reviews = Review.objects.filter(RestaurantID=restaurant_id)
    return render(request, 'reviews_template.html', {'reviews': reviews})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, ReviewID=review_id)
    review.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, ReviewID=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            modified_review = form.save(commit=False)  # Save the form, but don't commit to database yet

            # Append 'Edited' with the datetime stamp to the Description if it's been modified
            if 'Description' in form.changed_data:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Formatting the datetime
                modified_review.Description += "\n\n(Edited on {})\n".format(current_time)

            modified_review.save()
            return redirect('some_view_name')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review_template.html', {'form': form})
