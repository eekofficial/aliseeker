# Generated by Django 2.1 on 2018-10-24 19:03

from django.db import migrations
import main.models.models
import main.models.preferences


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_auto_20181023_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='referral_program_back_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка назад, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_back_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка назад, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_balance_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка баланса, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_balance_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка баланса, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_conditions_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка условий реферальной программы, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_conditions_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка условий реферальной программы, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_get_referral_link_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка получения реферальной ссылки, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_get_referral_link_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка получения реферальной ссылки, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_invite_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка приглашения, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_invite_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка приглашения, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_rating_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка рейтинга, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_rating_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка рейтинга, RU'),
        ),
        migrations.AlterField(
            model_name='media',
            name='welcome_gif_en',
            field=main.models.preferences.GIF(blank=True, null=True, upload_to=main.models.preferences.MediaFile.get_path, validators=[main.models.preferences.MediaFile.validate_media], verbose_name='Приветственная GIF-ка, EN'),
        ),
        migrations.AlterField(
            model_name='media',
            name='welcome_gif_ru',
            field=main.models.preferences.GIF(blank=True, null=True, upload_to=main.models.preferences.MediaFile.get_path, validators=[main.models.preferences.MediaFile.validate_media], verbose_name='Приветственная GIF-ка, RU'),
        ),
        migrations.AlterField(
            model_name='media',
            name='welcome_video_en',
            field=main.models.preferences.Video(blank=True, null=True, upload_to=main.models.preferences.MediaFile.get_path, validators=[main.models.preferences.MediaFile.validate_media], verbose_name='Приветственное MP4 видео, EN'),
        ),
        migrations.AlterField(
            model_name='media',
            name='welcome_video_ru',
            field=main.models.preferences.Video(blank=True, null=True, upload_to=main.models.preferences.MediaFile.get_path, validators=[main.models.preferences.MediaFile.validate_media], verbose_name='Приветственное MP4 видео, RU'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=main.models.models.Image(blank=True, null=True, upload_to=main.models.models.Image.get_path, validators=[main.models.models.Image.validate_image], verbose_name='Изображение снизу (до 1МБ)'),
        ),
    ]
