from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where mobileNo is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, mobileNo, password, **extra_fields):
        """
        Create and save a User with the given mobileNo and password.
        """
        if not mobileNo:
            raise ValueError(_('The mobileNo is required to register'))
        user = self.model(mobileNo=mobileNo, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, mobileNo, password, **extra_fields):
        """
        Create and save a SuperUser with the given mobileNo and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_admin', True)

        return self.create_user(mobileNo, password, **extra_fields)
