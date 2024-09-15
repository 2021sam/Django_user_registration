import logging
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

class EmailVerificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            logger.debug(f"Authenticated user: {request.user.email}")
            if not request.user.is_active:
                logger.debug(f"Inactive user: {request.user.email}, redirecting to verification.")
                return redirect('resend_verification')
        return self.get_response(request)








# from django.shortcuts import redirect
# import logging

# logger = logging.getLogger(__name__)

# class EmailVerificationMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             logger.info('**************************************')
#             logger.info(f"User {request.user.email} is authenticated.")
#             if not request.user.is_active:
#                 logger.info(f"User {request.user.email} is inactive. Redirecting to verification.")
#                 return redirect('resend_verification')
#         return self.get_response(request)
