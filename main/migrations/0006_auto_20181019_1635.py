# Generated by Django 2.1 on 2018-10-19 16:35

from django.db import migrations
import main.models.preferences


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_botuser_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='welcome_message_en',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Приветственное сообщение, EN'),
        ),
        migrations.AddField(
            model_name='settings',
            name='welcome_message_ru',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Приветственное сообщение, RU'),
        ),
    ]
