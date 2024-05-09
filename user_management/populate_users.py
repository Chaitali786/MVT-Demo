import os
import django
from faker import Faker
from user_management.users.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')
django.setup()

fake = Faker()

def create_fake_users(num_users):
    for _ in range(num_users):
        User.objects.create(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )

if __name__ == '__main__':
    create_fake_users(2)  # Change the number of users as needed
