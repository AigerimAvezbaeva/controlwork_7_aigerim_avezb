# Generated by Django 4.1.6 on 2023-02-25 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guestbook',
            options={'ordering': ['-created_at'], 'verbose_name': 'Запись гостевой книги', 'verbose_name_plural': 'Записи гостевой книги'},
        ),
    ]
