from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login_urlpattern')
    template_name = 'travelsale/signup.html'

    def post(self, request, *args, **kwargs):
        pass
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name='ci_customer')
            user.groups.add(user_group)
            return redirect('login_urlpattern')
        else:
            return render(request, self.template_name, {'form' : form })