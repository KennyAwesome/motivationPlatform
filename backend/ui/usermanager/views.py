from django.contrib.auth import  authenticate, login
from django.shortcuts import render
from django.views.generic import View

from .forms import LoginForm
from .forms import RegisterForm


#from django.context_processor import csrf
#from .models import # will be tokens
# Create your views here.
#album = get_object_or_404(Album, pk=album_id)

#class IndexView(generic.ListView):
#    template_name = 'usermanager/templates/index.html'
#    def get_queryset(self):
#        return HttpResponse("<h1>Basic User thingy works</h1>")
class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        #form = self.form_class(None)
        return render(request, self.template_name, "")

class LoginView(View):
    template_name = 'login.html'
    form_class = LoginForm  # the blueprint

    # display blank form -> no account
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST) # hier is already validation
        context = {'loggedIn': False, 'message': ""}

        if form.is_valid():
            # normalize data, proper format
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            return render(request, "index.html", context)
            if user is not None:
                if user.is_active:
                    login(request, user) # now logged in
                    context = {'loggedIn': True}
                    return render(request, "index.html", context)
                else:
                    context = {'loggedIn': False, 'message': "User is not active"}
                    return render(request, "index.html", context)
            else:
                    context = {'loggedIn': False, 'message': "None user"}
                    return render(request, "index.html", context)
        else:
            context = {'loggedIn': False, 'message': "Invalid Form"}
            return render(request, "index.html", context)
                    #request.user.username
                    # should redirect, not to show blank page

class RegisterView(View):
    form_class = RegisterForm # the blueprint
    template_name = 'form_registration.html'
    # class based views

    # display blank form -> no account
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data, adding user
    def post(self, request):
        form = self.form_class(request.POST) # hier is already validation

        if form.is_valid():
            user = form.save(commit=False) # creates a form from object, not in db yet

            # normalize data, proper format
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # set password etc., they are not txt, they are hashes
            user.set_password(password)
            user.save()
            #user.is_active = True  # should be done by email and activation ticket, but just for prototyping
            #user.save()

            #authenticate
            user = authenticate(username=username, password=password)

            context = {'loggedIn': False}
            if user is not None:
                if user.is_active:
                    login(request, user) # now logged in
                    context = {'loggedIn': True}
                    return render(request, "index.html", context)
                else:
                    return render(request, "index.html", context)
            else:
                    return render(request, "index.html", context)
                    #request.user.username
                    # should redirect, not to show blank page