from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, personal_account, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not personal_account:
            raise ValueError("The given personal account must be set")
        user = self.model(personal_account=personal_account, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, personal_account, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_client", True)
        extra_fields.setdefault("is_manager", False)

        return self._create_user(personal_account, password, **extra_fields)

    def create_superuser(self, personal_account, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(personal_account, password, **extra_fields)
