# Generated by Django 4.2.3 on 2023-07-09 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_book_film'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='isbn',
        ),
    ]
