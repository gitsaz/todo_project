from django.contrib.auth.base_user import BaseUserManager

class UserManagerForm(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("Enter a username")
        if not email:
            raise ValueError("enter a email")
        if not password:
            raise ValueError("Enter a password")
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        return self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )