# Generated by Django 2.1 on 2018-10-20 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20181020_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Link', verbose_name='Ссылка на AliExpress'),
        ),
    ]
