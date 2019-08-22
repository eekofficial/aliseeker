# Generated by Django 2.1 on 2018-10-30 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import tickets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0030_auto_20181030_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketdialogue',
            name='form_image',
            field=tickets.models.Image(blank=True, null=True, upload_to=tickets.models.Image.get_path, validators=[tickets.models.Image.validate_image], verbose_name='Изображение снизу (до 1 МБ)'),
        ),
        migrations.AlterField(
            model_name='ticketdialogue',
            name='last_message_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 30, 14, 2, 24, 509239, tzinfo=utc), verbose_name='Время последнего сообщения (часовой пояс UTC)'),
        ),
    ]