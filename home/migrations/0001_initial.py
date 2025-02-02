# Generated by Django 3.2.25 on 2024-04-06 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(choices=[('Employee', 'Employee'), ('Business', 'Business'), ('Student', 'Student'), ('Others', 'Others')], max_length=10)),
                ('savings', models.IntegerField(blank=True, null=True)),
                ('income', models.BigIntegerField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddMoneyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_money', models.CharField(choices=[('Expense', 'Expense'), ('Income', 'Income')], max_length=10)),
                ('amount', models.BigIntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('Food', 'Food'), ('Travel', 'Travel'), ('Shopping', 'Shopping'), ('Necessities', 'Necessities'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], default='Food', max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'addmoney',
            },
        ),
    ]
