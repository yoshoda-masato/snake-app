# Generated by Django 3.0.3 on 2020-06-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snake', '0005_auto_20200620_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='日付'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='nextdate',
            field=models.DateTimeField(auto_now=True, verbose_name='次回日付'),
        ),
    ]
