# Generated by Django 4.2.7 on 2023-12-21 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactUsMessage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactusmessage',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contact Phone'),
        ),
        migrations.AlterField(
            model_name='contactusmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='создано в: '),
        ),
    ]