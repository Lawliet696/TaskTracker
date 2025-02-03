from django.contrib.auth.views import LoginView
from .forms import LoginForm
from django.shortcuts import render, get_object_or_404

from .models import Profile, User

def show_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    context = {
        'profile': profile,
    }

    return render(request, 'accounts/profile.html', context=context)

class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True

        return super(CustomLoginView, self).form_valid(form)
