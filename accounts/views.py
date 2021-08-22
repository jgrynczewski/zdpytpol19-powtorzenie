from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('login'))

    return render(
        request,
        'registration/register.html',
        context = {
            'form': form
        }
    )