# Generated by Django 2.1 on 2018-10-23 20:36

from django.db import migrations
import main.models.models
import main.models.preferences


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20181023_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='referral_program_conditions_message_en',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Условия реферальной программы, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_conditions_message_ru',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Условия реферальной программы, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_invitation_button_label_en',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка приглашения, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_invitation_button_label_ru',
            field=main.models.preferences.BotButtonLabel(default='-', max_length=50, verbose_name='Кнопка приглашения, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_invitation_message_en',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Приглашение, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_invitation_message_ru',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Приглашение, RU'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_message_en',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Сообщение реферальной программы, EN'),
        ),
        migrations.AddField(
            model_name='texts',
            name='referral_program_message_ru',
            field=main.models.preferences.BotMessage(default='-', max_length=4000, verbose_name='Сообщение реферальной программы, RU'),
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
