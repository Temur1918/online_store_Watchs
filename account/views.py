from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from account.forms import UserRegistrationForm, LoginForm, UserEditForm, ProfileEditForm, ContactForm
from account.models import Profile, ContactModel
from viewapp.models import WatchModel

# Create your views here.

# def user_register(request):
#     if request.method == "POST":
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(
#                 user_form.cleaned_data["password"]
#             )
#             new_user.save()
#             context = {
#                 "new_user" : new_user,
#             }
#             return HttpResponse("<h2>Success</h2>")
#             # return render(request, "pages/register.html", context)
#             # # return render(request, 'pages/register.html', context_instance=RequestContext(request))

#     else:
#         user_form = UserRegistrationForm()    
#     context = {
#         "user_form" : user_form,
#     }
#     return render(request, "pages/register.html", context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST) 
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data["password"]
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            # context = {
            #     "new_user" : new_user,
            # }
            # return render(request, 'pages/login.html', context)
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form" : user_form,
        }
        return render(request, 'pages/register.html', context)

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = "pages/register.html"

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,
                                password=data['password'],
                                username=data['username'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("<h2>Success<h2>")
                else:
                    return HttpResponse("<h2>Profilingiz faol holatda emas</h2>")
            else:
                return HttpResponse("Login yoki parol xato")
    else:
        form = LoginForm()
        context = {
            "form" : form
        }
        return render(request, 'pages/login.html', context)
    
@login_required
def profile(request):
    user_form = request.user
    context = {
        "user_form" : user_form
    }
    return render(request, "pages/profile.html", context)


class ProfileEdit(LoginRequiredMixin, View):
    success_url = reverse_lazy('home_page_view')

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        context = {
            "user_form" : user_form,
            "profile_form" : profile_form
        }
        return render(request, "pages/profile_edit.html", context)

    def post(self, request):
        if request.method == "POST":
            user_form = UserEditForm(instance=request.user, data=request.POST)
            profile_form = ProfileEditForm(instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('profile')
        return render(request, "pages/profile_edit.html", { "user_form" : user_form, "profile_form" : profile_form })
    

class ContactView(CreateView):
    template_name = "pages/contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            "form": form
        }
        return render(request, "pages/contact.html", context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return redirect('home_page_view')
            # return HttpResponse("<h2>Malumotlaringiz muvaffaqiyatli junatildi!</h2>")

        context = {
            "form" : form
        }
        return render(request, "pages/contact.html", context)
    
