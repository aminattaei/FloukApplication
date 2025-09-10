# Import Django admin and the built-in User and Group models
from django.contrib import admin
from django.contrib.auth.models import Group, User

# Import the custom Profile model (linked to User via OneToOneField)
from .models import Profile

# Unregister the default Group and User models from the admin site
admin.site.unregister(Group)
admin.site.unregister(User)

# Define an inline admin to display/edit the Profile within the User admin page
class ProfileInline(admin.StackedInline):
    model = Profile  # Specify the related model

# Create a custom admin class for the User model
@admin.register(User)  # Register this custom admin with the User model
class UserAdmin(admin.ModelAdmin):
    model = User  # Set the model for this admin
    fields = ["username"]  # Only display the username field in the form
    inlines = [ProfileInline]  # Include the Profile form inline with the User form
