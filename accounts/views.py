from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserRegistrationForm, UserLoginForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.models import Post
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET
stripe.api_base = settings.STRIPE_BASE_URL


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=1999,
                    currency="USD",
                    description=form.cleaned_data['email'],
                    source=form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined")

            if customer.paid:
                form.save()
                user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))

                if user:
                    auth.login(request, user)
                    messages.success(request, "You have successfully registered")
                    return redirect(reverse('profile'))

                else:
                    messages.error(request, "unable to log you in at this time!")
            else:
                messages.error(request, "We were unable to take payment with that card")

    else:
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))

    return render(request, 'register.html', args)


@login_required(login_url='/login/')
def profile(request):
    posts = Post.objects.filter(created_on__lte=timezone.now()).order_by('-created_on')
    return render(request, 'profile.html', {'posts': posts})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, 'You have successfully logged in! ')
                return redirect(reverse('profile'))
            else:
                form.add_error(None, 'Your email or password was not recognised')
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)


@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
