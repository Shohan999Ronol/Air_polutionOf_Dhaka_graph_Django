# Generated by Django 4.1 on 2022-08-25 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_database_delete_line_charts1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='database',
        ),
    ]