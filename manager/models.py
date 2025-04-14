from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Security consideration: Don't store encryption key in code
# Instead, use environment variables or a secure configuration management system

def validate_encryption_key(value):
    if not value:
        raise ValidationError("Encryption key is required for password storage.")

class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link entries to users
    website = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    encrypted_password = models.CharField(max_length=255)  # Store encrypted password

    def __str__(self):
        return f"{self.user.username} - {self.website}"  # Display entry details

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        try:
            # Attempt decryption to ensure encryption key is valid
            self.get_password()
        except (ValueError, TypeError):
            raise ValidationError("Invalid encryption key. Please ensure it's configured correctly.")

    def set_password(self, raw_password):
        # Replace with secure encryption using a reputable library like cryptography.fernet
        # This example is for demonstration purposes only
        encrypted_password = raw_password  # Placeholder, replace with actual encryption
        self.encrypted_password = encrypted_password

    def get_password(self):
        # Replace with secure decryption using a reputable library like cryptography.fernet
        # This example is for demonstration purposes only
        decrypted_password = self.encrypted_password  # Placeholder, replace with actual decryption
        return decrypted_password

