# Generated by Django 5.0.7 on 2024-07-29 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_role_user_delete_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': []},
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.ManyToManyField(blank=True, related_name='users', to='accounts.role'),
        ),
    ]
