from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.middleware.csrf import get_token
from allauth.account.views import (
    SignupView, LogoutView, PasswordResetView, PasswordResetDoneView, LoginView, 
    PasswordChangeView, EmailVerificationSentView
)
from django.contrib.auth.views import PasswordResetConfirmView

def htmx_component(request, component, props=None):
    if props is None:
        props = {}

    # Retrieve CSRF token
    csrf_token = get_token(request)
    props['csrf_token'] = csrf_token
    
    if request.META.get('HTTP_HX_REQUEST'):
        print("============================== HTMX is available ==============================")
        return render(request, component, props)
    else:
        print("============================== HTMX is not available, rendering :", component+" ==============================")
        content = render_to_string(component, props)
        props['content'] = content
        return render(request, 'base.html', props)

def index(request):
    return htmx_component(request, "home.html")

def catimages(request):
    return htmx_component(request, 'images.html')

def about(request):
    props = {
        'username': 'ymlik',
        'greeting': 'Hello, World!',
        'description': 'Welcome to the homepage.'
    }
    return htmx_component(request, "about.html", props)


def profile(request):
    if request.user.username != "":
        props = {
            'username': request.user.username,
            'email': request.user.email
        }
    else:
        return redirect("/accounts/login")
    return htmx_component(request, 'account/profile.html', props)

def login(request):
    if request.method == 'GET':
        return htmx_component(request, 'account/login.html')
    else:
        # For POST requests, redirect to the allallauth login view
        view = LoginView.as_view()(request)
        # Check if the form submission is valid
        if view.status_code == 302:
            # If valid, redirect as normal (handled by CustomSignupView)
            return view
        else:
            # If not valid, re-render the signup page with errors
            return htmx_component(request, 'account/login.html', view.context_data)

class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Save the user
        self.user, resp = form.try_save(self.request)
        if resp:
            return resp
        
        # Redirect to the login page after successful signup
        return redirect('account_login')
def signup(request):
    if request.method == 'GET':
        return htmx_component(request, 'account/signup.html')
    else:
        view = CustomSignupView.as_view()(request)
        
        # Check if the form submission is valid
        if view.status_code == 302:
            # If valid, redirect as normal (handled by CustomSignupView)
            return view
        else:
            # If not valid, re-render the signup page with errors
            return htmx_component(request, 'account/signup.html', view.context_data)

def logout(request):
    if request.method == 'GET':
        return htmx_component(request, 'account/logout.html')
    else:
        return LogoutView.as_view()(request)
    
def confirm_logout(request):
    if request.method == 'POST':
        logout(request)  # Logs the user out
        return redirect(reverse('account_login')) 

def password_reset(request):
    if request.method == 'GET':
        return htmx_component(request, 'account/password_reset.html')
    else:
        return PasswordResetView.as_view()(request)
    
    
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'
def password_reset_done(request):
    if request.method == 'GET':
        return htmx_component(request, 'account/password_reset_done.html')
    else:
        view = CustomPasswordResetDoneView.as_view()(request)
        if view.status_code == 302:
            # If valid, redirect as normal (handled by CustomSignupView)
            return view
        else:
            # If not valid, re-render the signup page with errors
            return htmx_component(request, 'account/password_reset_done.html', view.context_data)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    success_url = reverse_lazy('account_login')  # Redirect after password reset
def password_reset_confirm(request, uidb64, token):
    if request.method == 'GET':
        # Handle the GET request and render the page with your custom template
        return htmx_component(request, 'account/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})
    else:
        # Handle POST request, form submission, etc.
        return CustomPasswordResetConfirmView.as_view()(request, uidb64=uidb64, token=token)
    
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_from_key.html'

    def form_valid(self, form):
        # You can add custom behavior here if needed
        return super().form_valid(form)


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account_profile')  # Redirect to the profile page after a successful password change
def password_change(request):
    if request.method == 'GET':
        return htmx_component(request, 'account/password_change.html')
    else:
        return CustomPasswordChangeView.as_view()(request)

def email_confirm(request, key=None):
    if request.method == 'GET':
        return htmx_component(request, 'account/email_confirm.html', {'key': key})
    else:
        return EmailVerificationSentView.as_view()(request, key=key)


def images(request):
    if request.method == 'GET':
        return htmx_component(request, 'images.html')
    
def loaded_images(request):
    if request.method == 'GET':
        return htmx_component(request, 'loaded-images.html')


def new_image_view(request, image_id):
    image_url = f"/static/img/8K/0{image_id}.jpg"  # Adjust according to your images
    img_tag = f'<img class="w-full h-full object-cover" src="{image_url}" alt="">'
    return HttpResponse(img_tag)



"""

def index2(request):
    content = render_to_string('home.html', {})
    return render(request, 'base.html', {'content': content, 'title': 'Home'})

def about2(request):
    content = render_to_string('about.html', {})
    return render(request, 'base.html', {'content': content, 'title': 'About'})

"""