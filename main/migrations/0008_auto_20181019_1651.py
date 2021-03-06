# Generated by Django 2.1 on 2018-10-19 16:51

from django.db import migrations
import main.models.preferences


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20181019_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='feedback_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка обратной связи, EN'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='feedback_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка обратной связи, RU'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='referral_program_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка реферальной программы, EN'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='referral_program_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка реферальной программы, RU'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='seeker_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка поиска товара, EN'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='seeker_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка поиска товара, RU'),
        ),
    ]
