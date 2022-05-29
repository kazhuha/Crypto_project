from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('portfolio:index')
