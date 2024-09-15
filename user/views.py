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

# from django.shortcuts import render

# Home view
def home(request):
    return render(request, 'user/home.html')



# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import send_mail
# from django.utils.http import urlsafe_base64_encode
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.contrib.sites.shortcuts import get_current_site
# from .models import CustomUser

# def send_verification_email(request, user):
#     token = default_token_generator.make_token(user)
#     uidb64 = urlsafe_base64_encode(force_bytes(user.pk))  # Correct the name to uidb64
#     current_site = get_current_site(request)
#     subject = 'Verify Your Email Address'
#     message = render_to_string('user/verify_email.html', {
#         'user': user,
#         'domain': current_site.domain,
#         'uidb64': uidb64,  # Make sure it's uidb64 here as well
#         'token': token,
#     })
#     send_mail(subject, message, 'no-reply@yourdomain.com', [user.email])

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser








import logging
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

logger = logging.getLogger(__name__)

def custom_login(request):
    logger.debug("Login view accessed")

    if request.method == 'POST':
        logger.debug("POST request received")
        form = AuthenticationForm(request, data=request.POST)

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
                    messages.warning(request, 'Your account is inactive. Please verify your email.')
                    return redirect('resend_verification')  # Redirect to the verification page
            else:
                logger.debug(f"Authentication failed for {username}")
                messages.error(request, 'Invalid email or password.')
        else:
            logger.debug("Login form is invalid")
            logger.debug(f"Form errors: {form.errors}")
            messages.error(request, 'Please correct the errors below.')
    else:
        logger.debug("GET request received, rendering login form")
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})







# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages

# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')

#             # Authenticate the user using the custom backend
#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     # If user is active, log them in
#                     login(request, user)
#                     return redirect('home')  # Redirect to home page
#                 else:
#                     # If user is inactive, redirect to resend verification page
#                     messages.warning(request, 'Your account is inactive. Please verify your email.')
#                     return redirect('resend_verification')  # Redirect to the verification page
#             else:
#                 # If authentication fails
#                 messages.error(request, 'Invalid email or password.')
#         else:
#             # If the form is invalid
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'registration/login.html', {'form': form})







# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages

# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
            
#             # Authenticate the user using the custom backend
#             user = authenticate(request, username=username, password=password)
            
#             if user is not None:
#                 if user.is_active:
#                     # If user is active, log them in and redirect to the home page
#                     login(request, user)
#                     return redirect('home')  # Adjust 'home' to your actual home page URL
#                 else:
#                     # If user is inactive, redirect to the resend verification page
#                     messages.warning(request, 'Your account is inactive. Please verify your email.')
#                     return redirect('resend_verification')  # Redirect to the verification page
#             else:
#                 # If authentication failed
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             # If the form is invalid
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = AuthenticationForm()

#     return render(request, 'registration/login.html', {'form': form})




# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages

# def custom_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('home')  # Redirect to the home page
#                 else:
#                     messages.warning(request, 'Your account is inactive. Please verify your email.')
#                     return redirect('resend_verification')  # Redirect to resend verification page
#             else:
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             messages.error(request, 'Please correct the error below.')
    
#     else:
#         form = AuthenticationForm()

#     return render(request, 'registration/login.html', {'form': form})





def send_verification_email(request, user):
    # Generate token and uid for the verification link
    token = default_token_generator.make_token(user)
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    
    # Get the current site for the email link
    current_site = get_current_site(request)
    
    # Render the email template with the verification link
    html_content = render_to_string('user/verify_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uidb64': uidb64,
        'token': token,
    })
    
    # Strip the HTML tags to create a plain text version
    text_content = strip_tags(html_content)
    
    # Set up the email
    subject = 'Verify Your Email Address'
    from_email = 'no-reply@yzyxe.biz'
    to_email = user.email
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    
    # Attach the HTML version
    email.attach_alternative(html_content, "text/html")
    
    # Send the email
    email.send()



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

@login_required
def resend_verification_email(request):
    user = request.user
    if not user.is_active:
        # Call the function that sends the verification email
        send_verification_email(request, user)
        messages.success(request, 'A new verification email has been sent.')
        return redirect('home')  # Redirect to home or another page
    else:
        messages.info(request, 'Your account is already verified.')
        return redirect('home')







def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            send_verification_email(request, user)
            messages.success(request, 'A verification email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterForm()

    return render(request, 'user/register.html', {'form': form})




# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_str
# from django.contrib.auth.models import User
# from django.shortcuts import redirect
# from django.contrib import messages

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
        return redirect('login')
    else:
        messages.error(request, 'The activation link is invalid or has expired.')
        return redirect('sign_up')









# # views.py
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login
# from .forms import RegisterForm
# from .models import CustomUser


# from django.shortcuts import render

# # Home view
# def home(request):
#     return render(request, 'user/home.html')




# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import login
# from .forms import RegisterForm
# from .models import CustomUser

# def sign_up(request):
#     if request.method == 'GET':
#         form = RegisterForm()
#         return render(request, 'user/register.html', {'form': form})

#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Automatically log the user in
#             messages.success(request, 'You have successfully signed up.')
#             return redirect('home')  # Redirect to the home page or another view
#         else:
#             messages.error(request, 'Please correct the errors below.')
#             return render(request, 'user/register.html', {'form': form})
