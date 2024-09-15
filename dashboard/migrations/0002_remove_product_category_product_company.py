# Generated by Django 5.0.7 on 2024-09-15 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(choices=[('Mountain Dew', 'Mountain Dew'), ('Pepsi', 'Pepsi'), ('Sprite', 'Sprite'), ('Coca Cola', 'Coca Cola'), ('RC', 'RC')], max_length=50, null=True),
        ),
    ]
