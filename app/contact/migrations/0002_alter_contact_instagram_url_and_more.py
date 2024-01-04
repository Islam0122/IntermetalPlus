# Generated by Django 4.2.8 on 2024-01-04 23:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='instagram_url',
            field=models.URLField(blank=True, help_text='URL для Instagram.', null=True, verbose_name='Ссылка на Instagram'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='telegram_url',
            field=models.URLField(blank=True, help_text='URL для Telegram.', null=True, verbose_name='Ссылка на Telegram'),
        ),
    ]
