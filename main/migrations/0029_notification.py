# Generated by Django 2.1 on 2018-10-20 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='active', max_length=16, verbose_name='Статус')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Link', verbose_name='Ссылка')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='main.BotUser', verbose_name='Пользователь')),
            ],
        ),
    ]