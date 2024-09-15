from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q



import logging
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

logger = logging.getLogger(__name__)

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.debug(f"Trying to authenticate user with email: {username}")
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(email=username))
        except UserModel.DoesNotExist:
            logger.debug(f"User with email {username} not found")
            return None

        if user.check_password(password):
            logger.debug(f"User {username} successfully authenticated")
            return user
        else:
            logger.debug(f"Password mismatch for user {username}")
            return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None





# import logging
# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model
# from django.db.models import Q

# logger = logging.getLogger(__name__)

# class EmailBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             # Log the attempt
#             logger.debug(f"Trying to authenticate user with email: {username}")
            
#             # Get user by email
#             user = UserModel.objects.get(Q(email=username))
#         except UserModel.DoesNotExist:
#             logger.debug(f"User with email {username} does not exist.")
#             return None

#         # Check if the password is correct
#         if user.check_password(password):
#             # Optionally, allow inactive users to authenticate (if you want to handle redirection in views)
#             logger.debug(f"User {username} authenticated, checking if active.")
#             return user  # Return the user whether active or not; check 'is_active' in the view
#         else:
#             logger.debug(f"Authentication failed for {username}: incorrect password.")
#             return None

#     def get_user(self, user_id):
#         UserModel = get_user_model()
#         try:
#             return UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None





# import logging

# logger = logging.getLogger(__name__)

# class EmailBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         logger.debug(f"Authenticating {username} using EmailBackend")
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(Q(email=username))
#         except UserModel.DoesNotExist:
#             return None

#         if user.check_password(password) and self.user_can_authenticate(user):
#             logger.debug(f"Authentication successful for {username}")
#             return user
#         logger.debug(f"Authentication failed for {username}")
#         return None





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

    # def get_user(self, user_id):
    #     UserModel = get_user_model()
    #     try:
    #         return UserModel.objects.get(pk=user_id)
    #     except UserModel.DoesNotExist:
    #         return None

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
