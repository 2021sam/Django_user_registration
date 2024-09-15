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



from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from .models import CustomUser

def resend_verification_email(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to resend the verification email.')
        return redirect('login')

    user = request.user
    # Check if the user is already active
    if user.is_active:
        messages.info(request, 'Your account is already activated.')
        return redirect('home')

    # Send the verification email
    send_verification_email(request, user)
    messages.success(request, 'A new verification email has been sent to your email address.')
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
