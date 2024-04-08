from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import from 'django.utils' instead of 'django.utils.timezone'


# Create your models here.

SELECT_CATEGORY_CHOICES = [
    ("Food", "Food"),
    ("Travel", "Travel"),
    ("Shopping", "Shopping"),
    ("Necessities", "Necessities"),
    ("Entertainment", "Entertainment"),
    ("Others", "Others"),
]

EXPENSE_CHOICES = [
    ("Expense", "Expense"),
    ("Income", "Income"),
]

PROFESSION_CHOICES = [
    ("Employee", "Employee"),
    ("Business", "Business"),
    ("Student", "Student"),
    ("Others", "Others"),
]


class Addmoney_info(models.Model):  # Capitalize 'Money' for consistency
    # Foreign key: It establishes a many-to-one relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Remove unnecessary default value

    # CharField(): It stores small and large size strings in the database.
    add_money = models.CharField(max_length=10, choices=EXPENSE_CHOICES)

    # BigIntegerField(): It can store numbers from -9223372036854775808 to 9223372036854775807 in the database.
    amount = models.BigIntegerField()

    # DateField(): It accepts date as input.
    date = models.DateField(default=timezone.now)  # Use 'timezone.now'

    category = models.CharField(max_length=20, choices=SELECT_CATEGORY_CHOICES, default='Food')

    class Meta:
        db_table = 'addmoney'  # Lowercase for database table name convention


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profession = models.CharField(max_length=10, choices=PROFESSION_CHOICES)

    # IntegerField(): It stores integer numbers in a database.
    savings = models.IntegerField(null=True, blank=True)

    income = models.BigIntegerField(null=True, blank=True)

    # ImageField(): It stores images in the database.
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username
