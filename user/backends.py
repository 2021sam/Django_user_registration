from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q



import logging

logger = logging.getLogger(__name__)

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.debug(f"Authenticating {username} using EmailBackend")
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            logger.debug(f"Authentication successful for {username}")
            return user
        logger.debug(f"Authentication failed for {username}")
        return None





# class EmailBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             # Authenticate user by email
#             user = UserModel.objects.get(Q(email=username))
#         except UserModel.DoesNotExist:
#             return None

#         if user.check_password(password) and self.user_can_authenticate(user):
#             return user

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False
        """
        return getattr(user, 'is_active', False)







# # backends.py
# from django.contrib.auth.backends import ModelBackend
# from .models import CustomUser

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = CustomUser.objects.get(email=username)  # Use email instead of username
#         except CustomUser.DoesNotExist:
#             return None
#         if user.check_password(password):
#             return user
#         return None
