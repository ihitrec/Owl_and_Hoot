from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserForm
from checkout.models import Order


def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST' and 'default_city' in request.POST:
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated')

    form = UserForm(instance=profile)
    orders = profile.orders.all()
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, 'profiles/profile.html', context)


def order_history(request, order_number):
    order = get_object_or_404(Order, pk=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)
