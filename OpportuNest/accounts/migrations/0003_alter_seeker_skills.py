# Generated by Django 5.1.2 on 2024-11-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_seeker_skills'),
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seeker',
            name='skills',
            field=models.ManyToManyField(to='skill.skill'),
        ),
    ]