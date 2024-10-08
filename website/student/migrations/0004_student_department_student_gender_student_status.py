# Generated by Django 4.0.4 on 2022-05-24 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_remove_student_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Department',
            field=models.CharField(choices=[('General', 'General'), ('Computer Science', 'Computer Science'), ('Information System', 'Information System'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Information Technology', 'Information Technology'), ('Decision Support', 'Decision Support')], default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Gender',
            field=models.BooleanField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Status',
            field=models.BooleanField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default=1),
            preserve_default=False,
        ),
    ]
