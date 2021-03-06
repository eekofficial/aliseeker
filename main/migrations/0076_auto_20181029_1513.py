# Generated by Django 2.1 on 2018-10-29 15:13

from django.db import migrations
import main.models.models
import main.models.preferences


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0075_auto_20181029_1330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botuser',
            old_name='balance_usd',
            new_name='balance',
        ),
        migrations.RenameField(
            model_name='botuser',
            old_name='total_earned_usd',
            new_name='total_earned',
        ),
        migrations.RenameField(
            model_name='botuser',
            old_name='total_withdrawn_usd',
            new_name='total_withdrawn',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='balance_rub',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='total_earned_rub',
        ),
        migrations.RemoveField(
            model_name='botuser',
            name='total_withdrawn_rub',
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
