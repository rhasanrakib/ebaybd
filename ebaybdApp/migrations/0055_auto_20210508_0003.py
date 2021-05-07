# Generated by Django 3.1.6 on 2021-05-08 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebaybdApp', '0054_volunteerregistration_accepted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerregistration',
            old_name='First_Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='volunteerregistration',
            name='Last_Name',
        ),
        migrations.RemoveField(
            model_name='volunteerregistration',
            name='district',
        ),
        migrations.AddField(
            model_name='volunteerregistration',
            name='designation',
            field=models.CharField(default='স্বেচ্ছাসেবক', help_text=' পদবী ', max_length=100),
        ),
        migrations.AddField(
            model_name='volunteerregistration',
            name='occupation',
            field=models.CharField(blank=True, help_text=' পেশা ', max_length=100),
        ),
        migrations.AddField(
            model_name='volunteerregistration',
            name='organization',
            field=models.CharField(blank=True, help_text=' প্রতিষ্ঠান ', max_length=100),
        ),
    ]
