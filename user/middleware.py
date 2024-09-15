from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)

class EmailVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            logger.info(f"User {request.user.email} is authenticated.")
            if not request.user.is_active:
                logger.info(f"User {request.user.email} is inactive. Redirecting to verification.")
                return redirect('resend_verification')
        return self.get_response(request)







# from django.shortcuts import redirect

# class EmailVerificationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated and not request.user.is_active:
#             # Redirect to a verification page or show the resend link
#             return redirect('resend_verification')  # Or a custom unverified page
#         return self.get_response(request)
