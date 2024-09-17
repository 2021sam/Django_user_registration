# /Users/2021sam/apps/authuser/user/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)






def waiting_for_approval(request):
    user = request.user
    return render(request, 'registration/waiting_for_approval.html', {'user': user})








# Home view
def home(request):
    return render(request, 'home.html')

@login_required
def profile(request):
    return render(request, 'user/profile.html')






from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate
def custom_login(request):
    logger.debug("Login view accessed")
    if request.method == 'POST':
        logger.debug("POST request received")
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            logger.debug("Login form is valid")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate the user using the custom backend
            user = authenticate(request, username=username, password=password)

            if user is not None:
                logger.debug(f"User {user.email} found")

                if user.is_active:
                    logger.debug(f"User {user.email} is active. Logging in.")
                    login(request, user)
                    return redirect('home')  # Redirect to the home page
                else:
                    logger.debug(f"User {user.email} is inactive. Redirecting to resend verification.")
                    # Store the email in the session for use in resend_verification
                    request.session['user_email'] = user.email
                    messages.warning(request, 'Your account is inactive. Please verify your email.')
                    # return redirect('resend_verification')  # Redirect to the verification page
                    return redirect("verify_account")  # # Redirect to the verification page
            else:
                logger.debug(f"Authentication failed for {username}")
                messages.error(request, 'Invalid email or password.')
        else:
            logger.debug("Login form is invalid")
            logger.debug(f"Form errors: {form.errors}")
            messages.error(request, 'Please correct the errors below.')
    else:
        logger.debug("GET request received, rendering login form")
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


from django.core.mail import EmailMessage

def send_verification_email(request, user):
    # Generate token and UID
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    # Build the absolute URL for email verification
    verification_url = request.build_absolute_uri(
        f"/user/activate/{uid}/{token}/"
    )

    # Render the email using the new HTML template
    subject = 'Verify your email address'
    message = render_to_string('emails/new_verification_email.html', {
        'user': user,
        'verification_url': verification_url,
    })

    # Create the email
    email = EmailMessage(
        subject,
        message,
        'no-reply@zyxe.biz',  # Replace with your email
        [user.email],
    )
    
    # Ensure email is sent as HTML
    email.content_subtype = "html"

    # Send the email
    email.send(fail_silently=False)


# No need for login_required since we're handling inactive users
def resend_verification_email(request):
    # Get the user's email from the session
    user_email = request.session.get('user_email', None)

    if user_email:
        try:
            # Fetch the user from the database using the email
            user = CustomUser.objects.get(email=user_email)
            if not user.is_active:
                # Logic to send the verification email
                send_verification_email(request, user)
                messages.success(request, 'A new verification email has been sent to your email address.')
                return redirect('home')  # Redirect to home after sending the email
            else:
                messages.info(request, 'Your account is already verified.')
                return redirect('home')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('login')
    else:
        return redirect('login')  # If the session does not have the email, redirect to login


def verify_account(request):
    user_email = request.session.get('user_email', None)

    if not user_email:
        # If no email is in the session, redirect to login
        return redirect('login')

    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(email=user_email)
            if not user.is_active:
                # Send the verification email
                send_verification_email(request, user)
                messages.success(request, 'A new verification email has been sent to your email address.')
                return redirect('login')  # Redirect to login after sending the email
            else:
                messages.info(request, 'Your account is already verified.')
                return redirect('home')
        except CustomUser.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('login')

    return render(request, 'registration/verify_account.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(request, user)
            messages.success(request, 'A verification email has been sent to your email address.')
            return redirect('waiting_for_approval')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully.')

        send_welcome_email(user)
        
        return redirect('login')
    else:
        messages.error(request, 'The activation link is invalid or has expired.')
        return redirect('sign_up')


from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import CustomUser

def send_welcome_email(user):
    # Prepare the email context (user info)
    subject = 'Welcome to Our Platform!'
    from_email = 'no-reply@zyxe.biz'
    to_email = [user.email]
    
    # Render the email template
    message = render_to_string('emails/welcome_email.html', {'user': user})
    
    # Create the email
    email = EmailMessage(subject, message, from_email, to_email)
    email.content_subtype = 'html'  # To send as HTML email
    
    # Send the email
    email.send(fail_silently=False)


from django.contrib.auth import logout

def custom_logout(request):
    logout(request)  # Logs the user out and clears the session
    return redirect('home')  # Redirects to home
