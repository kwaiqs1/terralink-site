import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create (or optionally update) a Django superuser from env vars."

    def handle(self, *args, **options):
        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL", "")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        # Optional: allow updating password if user already exists
        update_password = os.getenv("DJANGO_SUPERUSER_UPDATE_PASSWORD", "").lower() in {
            "1", "true", "yes", "y"
        }

        if not username or not password:
            self.stdout.write(
                self.style.WARNING(
                    "DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set — skipping superuser creation."
                )
            )
            return

        User = get_user_model()
        username_field = getattr(User, "USERNAME_FIELD", "username")
        lookup = {username_field: username}

        user = User.objects.filter(**lookup).first()

        if user:
            if update_password:
                user.set_password(password)
                # Ensure privileges
                if hasattr(user, "is_staff"):
                    user.is_staff = True
                if hasattr(user, "is_superuser"):
                    user.is_superuser = True
                if hasattr(user, "email") and email:
                    user.email = email
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Updated superuser '{username}'."))
            else:
                self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' already exists — skipping."))
            return

        # Create new superuser
        create_kwargs = {username_field: username}
        if hasattr(User, "email") and email:
            create_kwargs["email"] = email

        user = User.objects.create_superuser(**create_kwargs, password=password)
        self.stdout.write(self.style.SUCCESS(f"Created superuser '{username}'."))
