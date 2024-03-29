# Generated by Django 2.2.3 on 2019-07-26 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_height', models.IntegerField(verbose_name='身高(/cm)')),
                ('person_weight', models.IntegerField(verbose_name='体重(/kg)')),
                ('person_bmi', models.FloatField(max_length=4, verbose_name='BIM计算器')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
            ],
        ),
    ]
